import gradle_command_run
import pytest


def mock_call_command(command, **kwargs):
    print(command)
    return 0


class TestGradleCommandRun:

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, monkeypatch, capsys):
        self.monkeypatch = monkeypatch
        self.capsys = capsys

        monkeypatch.setattr("sys.exit", lambda code: code)
        monkeypatch.setattr("subprocess.call", mock_call_command)

    def test_simple_task(self):
        """
        Test with a simple Gradle task
        """

        self.monkeypatch.setenv("GRADLE_TASK", "check")

        gradle_command_run.main()

        assert "./gradlew check" in self.capsys.readouterr().out

    def test_with_default_arguments(self):
        """
        Test with Gradle task with default arguments
        """

        self.monkeypatch.setenv("GRADLE_TASK", "stageTest")
        self.monkeypatch.setenv("DEFAULT_ARGUMENTS", "--stacktrace")

        gradle_command_run.main()

        assert "./gradlew stageTest --stacktrace" in self.capsys.readouterr().out

    def test_with_extra_arguments(self):
        """
        Test with Gradle task with extra arguments
        """

        self.monkeypatch.setenv("GRADLE_TASK", "build")
        self.monkeypatch.setenv("GRADLE_EXTRA_ARGUMENTS", "--info")

        gradle_command_run.main()

        assert "./gradlew build --info" in self.capsys.readouterr().out

        self.monkeypatch.setenv("EXTRA_ARGUMENTS", "--stacktrace")

        gradle_command_run.main()

        assert "./gradlew build --stacktrace" in self.capsys.readouterr().out

    def test_on_main_branch(self):
        """
        Test with Gradle task on main branch
        """

        self.monkeypatch.setenv("GRADLE_TASK", "stageTest")
        self.monkeypatch.setenv("IS_MAIN_BRANCH", "true")

        gradle_command_run.main()

        assert "./gradlew stageTest -Pbuild.release" in self.capsys.readouterr().out

    def test_on_release_branch(self):
        """
        Test with Gradle task on release branch
        """

        self.monkeypatch.setenv("GRADLE_TASK", "stageTest")
        self.monkeypatch.setenv("IS_RELEASE_BRANCH", "true")

        gradle_command_run.main()

        assert "./gradlew stageTest -Pbuild.release" in self.capsys.readouterr().out

    def test_on_release_candidate_branch(self):
        """
        Test with Gradle task on release candidate branch
        """

        self.monkeypatch.setenv("GRADLE_TASK", "stageTest")
        self.monkeypatch.setenv("IS_RELEASE_CANDIDATE_BRANCH", "true")

        gradle_command_run.main()

        assert "./gradlew stageTest -Pbuild.candidate" in self.capsys.readouterr().out

    def test_with_all_options(self):
        """
        Test with Gradle task with default and extra arguments on a main branch
        """

        self.monkeypatch.setenv("GRADLE_TASK", "stageTest")
        self.monkeypatch.setenv("DEFAULT_ARGUMENTS", "--stacktrace")
        self.monkeypatch.setenv("GRADLE_EXTRA_ARGUMENTS", "--info")
        self.monkeypatch.setenv("IS_MAIN_BRANCH", "true")

        gradle_command_run.main()

        assert "./gradlew stageTest --stacktrace --info -Pbuild.release" in self.capsys.readouterr().out

    def test_system_exits_with_status_error_code(self):
        """
        Test the Python script will exit with same status code as the gradle command
        """

        return_code = 0

        def mock_exit(code):
            nonlocal return_code
            return_code = code

        def mock_error(*args, **kwargs):
            return -1

        self.monkeypatch.setattr("sys.exit", mock_exit)
        self.monkeypatch.setattr("subprocess.call", mock_error)

        self.monkeypatch.setenv("GRADLE_TASK", "error")

        gradle_command_run.main()

        assert return_code == -1


---- another test class

import find_gradle_artifact_file_path
import pytest
import os

DIST_SUBDIR = "build/distributions"


class TestFindGradleArtifactFilePath:

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, monkeypatch, capsys):
        self.monkeypatch = monkeypatch
        self.capsys = capsys

    @pytest.fixture(autouse=True)
    def setup_vars(self, monkeypatch, tmp_path):
        """
        Setup variables for all tests
        """

        monkeypatch.setenv("GITHUB_WORKSPACE", str(tmp_path))
        monkeypatch.setenv("GITHUB_ENV", str(tmp_path / "env"))

    def test_no_jar_or_war_files_found(self):
        """
        Test when no JAR or WAR files are found
        """

        with pytest.raises(Exception) as exception_info:
            find_gradle_artifact_file_path.main()

        assert "No 'app.jar' or 'app.war' files were found" in str(exception_info.value)

    def test_with_one_plain_jar_found(self):
        """
        Test with a single JAR file that is not called 'app.jar'
        """

        root_dir = os.environ['GITHUB_WORKSPACE']
        dist_dir = os.path.join(root_dir, DIST_SUBDIR)
        os.makedirs(dist_dir, exist_ok=True)
        with open(os.path.join(dist_dir, "my.jar"), 'w'):
            pass

        with pytest.raises(Exception) as exception_info:
            find_gradle_artifact_file_path.main()

        assert "No 'app.jar' or 'app.war' files were found." in str(exception_info.value)

    def test_both_jar_and_war_files_found(self):
        """
        Test when both JAR and WAR files are found
        """

        root_dir = os.environ['GITHUB_WORKSPACE']
        dist_dir = os.path.join(root_dir, DIST_SUBDIR)
        os.makedirs(dist_dir, exist_ok=True)
        with open(os.path.join(dist_dir, "app.jar"), 'w'):
            pass
        with open(os.path.join(dist_dir, "app.war"), 'w'):
            pass

        with pytest.raises(Exception) as exception_info:
            find_gradle_artifact_file_path.main()

        assert "We found both 'app.jar' and 'app.war' files in the 'distributions' directory" in str(exception_info.value)

    def test_more_than_one_application_jar_file_found(self):
        """
        Test when there are more than one JAR file
        """

        create_sub_modules_with_three_artifact_files(file_extension='jar')

        with pytest.raises(Exception) as exception_info:
            find_gradle_artifact_file_path.main()

        assert "We have found 3 'app.jar' files on this project" in str(exception_info.value)

    def test_more_than_one_application_war_file_found(self):
        """
        Test when there are more than one WAR file
        """

        create_sub_modules_with_three_artifact_files(file_extension='war')

        with pytest.raises(Exception) as exception_info:
            find_gradle_artifact_file_path.main()

        assert "We have found 3 'app.war' files on this project" in str(exception_info.value)

    def test_with_one_app_jar_found(self):
        """
        Test with a single JAR file called 'app.jar'
        """

        root_dir = os.environ['GITHUB_WORKSPACE']
        dist_dir = os.path.join(root_dir, DIST_SUBDIR)
        os.makedirs(dist_dir, exist_ok=True)
        with open(os.path.join(dist_dir, "app.jar"), 'w'):
            pass

        find_gradle_artifact_file_path.main()
        env = read_env_file()

        assert f"DOCKER_ARTIFACT_FILE_PATH={DIST_SUBDIR}/app.jar" in env

    def test_with_one_app_war_found(self):
        """
        Test with a single WAR file called 'app.war'
        """

        root_dir = os.environ['GITHUB_WORKSPACE']
        dist_dir = os.path.join(root_dir, DIST_SUBDIR)
        os.makedirs(dist_dir, exist_ok=True)
        with open(os.path.join(dist_dir, "app.war"), 'w'):
            pass

        find_gradle_artifact_file_path.main()
        env = read_env_file()

        assert f"DOCKER_ARTIFACT_FILE_PATH={DIST_SUBDIR}/app.war" in env


def create_sub_modules_with_three_artifact_files(file_extension):
    # Check if file extension is either 'jar' or 'war' and fail if not either:
    if file_extension not in ['jar', 'war']:
        raise ValueError("File extension must be either 'jar' or 'war'")

    root_dir = os.environ['GITHUB_WORKSPACE']
    artifact_file = f'app.{file_extension}'

    # Create "build/distributions" directory in the root
    dist_dir = os.path.join(root_dir, DIST_SUBDIR)
    os.makedirs(dist_dir, exist_ok=True)

    # Create an empty file "app.jar" inside the "build/distributions" directory in the root
    with open(os.path.join(dist_dir, artifact_file), 'w'):
        pass

    # Create "sub-module-1" and "sub-module-2" dirs in the root
    submodule1_dir = os.path.join(root_dir, "sub-module-1")
    os.makedirs(submodule1_dir, exist_ok=True)

    submodule2_dir = os.path.join(root_dir, "sub-module-2")
    os.makedirs(submodule2_dir, exist_ok=True)

    # Create "build/distributions" directory and an empty file "app.jar" inside "sub-module-1"
    dist_dir_submodule1 = os.path.join(submodule1_dir, DIST_SUBDIR)
    os.makedirs(dist_dir_submodule1, exist_ok=True)

    with open(os.path.join(dist_dir_submodule1, artifact_file), 'w'):
        pass

    # Create "build/distributions" directory and an empty file "app.jar" inside "sub-module-2"
    dist_dir_submodule2 = os.path.join(submodule2_dir, DIST_SUBDIR)
    os.makedirs(dist_dir_submodule2, exist_ok=True)

    with open(os.path.join(dist_dir_submodule2, artifact_file), 'w'):
        pass


def read_env_file():
    env_path = os.getenv('GITHUB_ENV')
    with open(env_path, "r") as env_file:
        return env_file.read()
