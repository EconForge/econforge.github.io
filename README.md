# EconForge website 

This repository hosts the source for the EconForge blog. 

The site is generated using [http://docs.getpelican.com/en/3.3.0/](http://docs.getpelican.com/en/3.3.0/) and employs the [pure][http://purepelican.com/] theme.


## Adding Content

All of the content for this site goes into the `content/` folder. Any markdown (extension `.md`) or ReStructuredText (extension `.rst`) file placed in this directory will be included in the website. I encourage the use of markdown to write posts, so I will use markdown for all examples here.

### Post metadata

At the top of each post you should include metadata that describes the post. An example of the beginning of a post is given below

```markdown
Title: My super title
Date: 2014-06-26 10:54
Category: python
Tags: pelican, example
Slug: my-super-post
Authors: Spencer Lyon
about_author: Creator of this site
email: spencerlyon2@gmail.com
Summary: Short version for index and feeds

## Section Title

This is a great post

### Subtitle

...
```

For posts on this site we will require each user to fill in the following keys:

* `Title` (will become url if slug is not given)
* `Date`
* `Authors` (should be one person, despite the plural 

We encourage contributors to also fill in the other fields for the following reasons:

* `Category`: An index will be created that lists all the posts in a given category. It would be great if each post had an associated category
* `Tags`: An index will be created for each tag also. Think of this as a more specific version of the Category. For example, if I wrote a post about solving the neo-classical growth model using simple value function iteration in python I might set the Category equal to `python` and tags for `vfi, growth-model`.
* `about_author`: On the left hand side of the article view your name will appear. If you fill in this section the subtitle will appear below your name. This gives readers an idea of who you are.
* `email`: If this is specified, on the LHS of an article the [gravatar](http://en.gravatar.com/) associated with the given email will be included.
* `Summary`: This will appear under the post title in the list of posts on the front page of the website as well as in rss feeds.

### Including ipython notebooks

We can easily include all or parts of iPython notebooks in this blog. To do this we will use the [`liquid_tags`](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags) plugin. The syntax is as follows

```
{% notebook filename.ipynb %}
```

where `filename.ipynb` is the name of an ipython notebook you have included in the `content/downloads/notebooks` directory of this blog. There is also an optimal argument that lets you specify which cells from the notebook should be included in the post. This syntax uses python slicing notation and looks like this:

```
{% notebook filename.ipynb cells[2:] %}
```

In this case, pelican would skip the first 2 cells of the notebook and render the rest of them normally.

The `liquid_tags` plugin comes with a few other useful snippets like that, so I encourage you to take a peek at its (brief) documentation




