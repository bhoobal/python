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
