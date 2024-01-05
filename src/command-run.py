import os
import subprocess
import sys


def main():
    gradle_command = "./gradlew " + os.environ["GRADLE_TASK"]
    default_args = os.getenv("DEFAULT_ARGUMENTS")
    extra_args = os.getenv("EXTRA_ARGUMENTS") or os.getenv("GRADLE_EXTRA_ARGUMENTS")

    if default_args:
        gradle_command += " " + default_args

    if extra_args:
        gradle_command += " " + extra_args

    if "true" in [os.getenv("IS_MAIN_BRANCH"), os.getenv("IS_RELEASE_BRANCH")]:
        gradle_command += " -Pbuild.release"

    if os.getenv("IS_RELEASE_CANDIDATE_BRANCH") == "true":
        gradle_command += " -Pbuild.candidate"

    print(gradle_command, flush=True)
    sys.exit(subprocess.call(gradle_command, shell=True))


if __name__ == "__main__":
    main()
