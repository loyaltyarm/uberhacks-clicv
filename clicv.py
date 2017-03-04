import click

def print_certifications(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('')
    click.echo(click.style('Title: MobileIron Certified Administrator', bold=True))
    click.echo('Issuer: MobileIron, Inc.')
    click.echo('Year: 2014')
    click.echo('')
    click.echo(click.style('Title: iOS 7 Basic Developer Certification', bold=True))
    click.echo('Issuer: Invasive Code, Inc.')
    click.echo('Year: 2013')
    click.echo('')
    click.echo(click.style('Title: Apple Certified Associate - Mac Integration 10.9', bold=True))
    click.echo('Issuer: Apple, Inc.')
    click.echo('Year: 2012')
    click.echo('')
    ctx.exit()

def print_education(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('')
    click.echo(click.style('Graduated: December 2013', bold=True))
    click.echo('School: Western Kentucky University')
    click.echo('Concentration: Masters, Engineering Technology Management')
    click.echo('')
    click.echo(click.style('Graduated: December 2009', bold=True))
    click.echo('School: Western Kentucky University')
    click.echo('Concentration: Bachelors, General Studies: Sociology')
    click.echo('')
    ctx.exit()

def print_experience(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('')
    click.echo(click.style('Time: January 2017 - Present', fg='green', bold=True))
    click.echo('Title: Sr. Systems Engineer')
    click.echo('Concentration: Developer Tools and Infrastructure')
    click.echo(click.style('Company: Uber Advanced Technologies Center', fg='green', bold=True))
    click.echo('')
    click.echo(click.style('Time: June 2014 - December 2016', bold=True))
    click.echo('Title: Sr. Systems Engineer')
    click.echo('Concentration: Mobile Developer Infrastructure')
    click.echo(click.style('Company: Uber Technologies, Inc.', bold=True))
    click.echo('')
    click.echo(click.style('Time: April 2012 - May 2014', bold=True))
    click.echo('Title: Technical Advisor')
    click.echo('Concentration: Enterprise Mobility Engineering')
    click.echo(click.style('Company: FedEx Services', bold=True))
    click.echo('')
    click.echo(click.style('Time: October 2007 - April 2012', bold=True))
    click.echo('Title: Network Specialist/Desktop Support Technician')
    click.echo('Concentration: IT Services')
    click.echo(click.style('Company: Western Kentucky University', bold=True))
    click.echo('')
    ctx.exit()

def print_patents(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('')
    click.echo('Title: Selecting a messaging protocol for transmitting data in connection with a location based service')
    click.echo('URL: https://www.google.com/patents/US20170012920')
    click.echo('')
    ctx.exit()

def print_skills(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('')
    click.echo(click.style('Systems Deployment', bold=True))
    click.echo('Endorsers: 35')
    click.echo('')
    click.echo(click.style('Virtualization', bold=True))
    click.echo('Endorsers: 23')
    click.echo('')
    click.echo(click.style('Troubleshooting', bold=True))
    click.echo('Endorsers: 38')
    click.echo('')
    click.echo(click.style('VMWare ESX', bold=True))
    click.echo('Endorsers: 23')
    click.echo('')
    ctx.exit()

@click.command()

# Some resume options
@click.option('--certifications', is_flag=True, callback=print_certifications,
              expose_value=False, is_eager=True, help='See a list of my certifications.')
@click.option('--education', is_flag=True, callback=print_education,
              expose_value=False, is_eager=True, help='See my educational achievements.')
@click.option('--experience', is_flag=True, callback=print_experience,
              expose_value=False, is_eager=True, help='Print a list of my past/present companies and roles.')
@click.option('--patents', is_flag=True, callback=print_patents,
              expose_value=False, is_eager=True, help='Check out my patents!')
@click.option('--skills', is_flag=True, callback=print_skills,
              expose_value=False, is_eager=True, help='Check out my key skills.')

# The resume functions
def cli():
	"""clicv enables my resume as an interactive command line tool"""
	click.echo('')
	click.echo(click.style('You must specify an argument! Try running with --help to see options.', fg='red', bold=True))
	click.echo('')
