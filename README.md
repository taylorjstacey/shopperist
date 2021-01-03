# Shopperist

Shopperist takes the ingredients from an online recipe and puts it into a shopping list on Todoist.

## Setups
Shopperist has two prerequisites to get started. 

### API Token
To interact with your Todoist account, you need a Todoist API token. To get your API token go to [https://todoist.com/prefs/integrations](https://todoist.com/prefs/integrations).

Copy the API Token and place it in the `config.json` file. `config.json` should look like so:
```
{
    "api-token": "ABCDEEFGAPITOKENTUVWXYZ"
}
```

### Initilize Shopperist
Shopperist requires a project titled `Shopperist`. To create the project, run the following command:

```
python shopperist.py init
```

Shopperist will notify you if the project already exists in Todoist.

At this time, multiple projects or alternate names are not supported. Please create an issue if this is a requested feature. 

## How to add recipes

Shopperist will accept a URL from a wide variety of online recipe sites. Recipes can be added with the `add` command.

For the full list of supported websites, please refer to the [recipe_scrapers](https://github.com/hhursev/recipe-scrapers) project.

### Example

```
python shopperist.py add https://www.seriouseats.com/recipes/2016/12/the-best-roast-potatoes-ever-recipe.html
```

## Support the project.
This project is open source under the GPLv3 license. You can support the project in three ways.
1. Submit feature and issue requests.
2. Submit a pull request for new features.
3. If you find this useful and would've donated money to this project, please donate to your local food bank.

## Thanks
This project uses the following projects python modules. Thank you to those development teams, your work took the vast majority of the heavy lifting out of this project.

[todoist-python](https://github.com/Doist/todoist-python)
[validators](https://github.com/kvesteri/validators)
[recipe_scrapers](https://github.com/hhursev/recipe-scrapers)
[click](https://github.com/pallets/click)