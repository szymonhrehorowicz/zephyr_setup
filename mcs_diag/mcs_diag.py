import click
import subprocess

BOARD_NAME = "mcs_diag"
PROJECT_DIR = "threads"
ECHO_COLOR = "cyan"


@click.command()
@click.option("--build", is_flag=True, help="Build application")
@click.option("--debug", is_flag=True, help="Build application as Debug type")
@click.option("--flash", is_flag=True, help="Flash application to the target")
@click.option("--serve", is_flag=True, help="Start debug server")
def mcs_diag_cli(build, debug, flash, serve):
    if build:
        info_str = "[BUILDING]"
        args = ["west", "build", "-b", BOARD_NAME, ".", "--"]

        if debug:
            args.append("-DCMAKE_BUILD_TYPE=Debug")
            info_str += "[DEBUG]"
        else:
            args.append("-DCMAKE_BUILD_TYPE=Release")
            info_str += "[RELEASE]"

        click.secho(info_str, fg=ECHO_COLOR, bold=True)

        subprocess.run(args, cwd=PROJECT_DIR, shell=False)

    if flash:
        click.secho("[FLASHING]", fg=ECHO_COLOR, bold=True)

        subprocess.run(["west", "flash"], cwd=PROJECT_DIR, shell=False)

    if serve:
        click.secho("[STARTING DEBUG SERVER]", fg=ECHO_COLOR, bold=True)

        subprocess.run(["west", "debugserver"], cwd=PROJECT_DIR, shell=False)
