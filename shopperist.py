import click
from todoist import TodoistAPI
from recipe_scrapers import scrape_me
import validators
import json

def openTodoist():
    f = open('config.json',) 
    config = json.load(f)
    f.close()

    if config['api-token']=='':
        print('Please add an API token to config.json')
        exit()

    api = TodoistAPI(token=config['api-token'])
    api.sync()
    return api

@click.group()
def cli():
    pass

@cli.command()
def init():
    api = openTodoist()
    click.echo('Initializing project...')
    for project in api.state['projects']:
        if project['name'] == 'Shopperist':
            print("Shopperist project already exists! You're ready to go.")
            quit()
    
    api.projects.add('Shopperist')
    api.commit()
    click.echo('We created the Shopperist project!')
    click.echo('Add recipes to Shopperist with python shopperist.py add')
    
@cli.command()
@click.argument('url')
def add(url):
    api = openTodoist()
    if validators.url(url):
        click.echo('Adding ' + url + '...')

        for project in api.state['projects']:
            if project['name'] == 'Shopperist':
                click.echo('Shopperist project found!')
                scraper = scrape_me(url)
                print('Found recipe ' + scraper.title())
                initial_item = api.items.add(scraper.title(), project_id=project['id'])
                for ingredient in scraper.ingredients():
                    api.items.add(ingredient, project_id=project['id'], parent_id=initial_item['id'])
                print('Saving to Todoist...')
                api.commit()
                quit()
        print("Shopperist Project doesn't exist in Todoist. Please run the init command before adding recipes.")
        quit()
    else:
        print('URL is not valid. Please resubmit.')

if __name__ == '__main__':
    cli()
