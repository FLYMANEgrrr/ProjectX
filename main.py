import os
import click


@click.command()
# @click.option('--all', help='Run all .feature files.')
def all():
    os.system("behave features\\sign_up.feature")
    os.system("behave features\\sign_in.feature")
    os.system("behave features\\dresses.feature")
    os.system("behave features\\forgot_pass.feature")
    os.system("behave features\\tops.feature")
    os.system("behave features\\cart.feature")


@click.command()
# @click.option('--logo', help='Run logo-presence.feature file.')
def logo():
    os.system("behave features\logo_presence.feature")


@click.command()
# @click.option('--sign_up', help='Run sign_up.feature file.')
def sign_up():
    os.system("behave features\sign_up.feature")


@click.command()
# @click.option('--sign_in', help='Run sign_in.feature file.')
def sign_in():
    os.system("behave features\sign_in.feature")


@click.command()
# @click.option('--contact_us', help='Run contact_us.feature file.')
def contact_us():
    os.system("behave features\contact_us.feature")


@click.command()
# @click.option('--dresses', help='Run dresses.feature file.')
def dresses():
    os.system("behave features\dresses.feature")


@click.command()
# @click.option('--tops', help='Run tops.feature file.')
def tops():
    os.system("behave features\\tops.feature")

@click.command()
#@click.option('--forgot_pass',help='Run forgot_pass.feature file.')
def forgot_pass():
    os.system("behave features\\forgot_pass.feature")

@click.command()
# @click.option('--tops', help='Run tops.feature file.')
def tops():
    os.system("behave features\\tops.feature")
@click.command()
# @click.option('--cart', help='Run cart.feature file.')
def cart():
    os.system("behave features\\cart.feature")
@click.group()
def main():
    pass


main.add_command(all)
main.add_command(sign_up)
main.add_command(sign_in)
main.add_command(dresses)
main.add_command(forgot_pass)
main.add_command(tops)
main.add_command(cart)
if __name__ == "__main__":
    main()
