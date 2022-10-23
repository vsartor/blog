#### This is a static website.

What you're reading right now is a post from a *static website*. A "static website" means the content you're consuming is "static," - meaning that the only thing my server is doing is delivering "constant" files to you.

In practice, this means, for example, that you won't find a comment section here. A comment section would suggest that you could enter some text into a form, send this form back to my server, and my server would store that comment in a database. Then, when other people accessed this page, it would need to fetch information from the database so that other people could see your comment.

To be clear, doing this kind of stuff has been easy for quite some time. Indeed, by the time I started understanding computers and blogs for the first time over a decade ago, it was already pretty standard.

So you could ask me: "Why build a static website in 2022?"

I can break it down into two reasons:

- *I don't need dynamic features.* As of this writing, I don't expect people to read - much less want to comment publicly - on stuff I write. And besides comment sections, I can't think of anything else that I'd like to do that would require dynamic access to a database, for example.
- *Low maintenance and cost.* A static website is super cheap to maintain; it serves HTML/CSS and a few compressed images. No processing, no databases. Further, in a world where I have a comment section where people want to post, I would need to moderate that content before publishing it on my domain.

#### Why a static website generator?

Okay, so this website is essentially just a bunch of different HTML files, one for each separate page you access here. This means one HTML page specifically for the blog's home, one specifically for this post, and one for every other post or page I ever want to create.

There are a lot of things that need to be repeated across different pages. First and foremost, the HTML head, where we include items such as the website name, description, links to fonts, CSS files (the things that tell your browser what colors and places things should be at), etc. 

There's also a sidebar (navigation bar on top if you're on mobile) repeated across every page of this website. Imagine if I copied and pasted this to every file and eventually wanted to change something. I'd need to visit each file to perform changes individually.

*Static website generators allow us to define templates.*

For example, I have a template for the HTML head and a template for the navigation bar. Further, I have a template for posts so that the content of each post gets copied into the template and generates a new HTML file, together with the proper HTML head and navigation bar.

If I ever change a link in the navigation bar, I just change it in the specific file I use for the navigation bar. Then, the website generator will appropriately copy it and add it to all the pages the next time I update my blog.

We essentially offload the copy-paste work to the "generator."

Further, typing up blogs in HTML would be a pain in the tail. Imagine having to wrap everything you want to be in italics with `<em> … </em>`. Or instead separating each paragraph by wrapping them with `<p> … </p>`. 

*A blog generator will also commonly allow the author to type and store things in Markdown* while converting the posts to HTML only when generating the published website.

#### Why build my own static website generator?

[Because why not ¯\_(ツ)_/¯](https://justforfunnoreally.dev/)

#### How does it work?

Well, for reference, [this is the source](https://github.com/vsartor/blog) that my generator receives to build the website you're accessing right now.

You will notice there are a few different folders and two files. So let's knock them out one by one.

```
.
├── templates
├── globals.spec
├── pages.spec
├── content
├── preview
├── line
└── static
```

#### Templates

Here are the HTML templates. As previously mentioned, they're primarily meant to be *reusable snippets of HTML pages*. However, *some are actual templates for building the final pages themselves*, using other templates as building blocks.

They can have two types of tokens: references to other templates or variables.

For example, let's say I have a template for the head and one for the navigation bar. Then, I also have a template for the home page itself. In the homepage template, I want to include both the head and the navigation bar. I could do it like so:

```
${head}

<body>
    ${navigation_bar}

    Specific content for the homepage goes here.
</body>
```

Further, different pages will have other titles, but I'd like them all to share the same head template. To solve this, I can have the head template include a variable `@{title}` in the title field so that whenever I create a page, I can attribute this variable to it. So, the correct title will be applied whenever the template is filled for a specific page.

Page-specific or global variables are referenced through `@{variable_name}`, other templates are referenced through `${template_name}`.

There is another type of variable specifically related to posts. If I create a post template (or want to include post information on the homepage, for example), I need my generator to understand what are the different parts of a post: what is its title, its content, date of writing, etc. Post-specific variables are predefined and they're referenced like `#{post-title}`, `#{post-url}`, `#{post-date}`, etc. 

I chose to use `#` instead of still using `@` for post variables because general variables defined through `@` can be anything, whereas post variables are predefined. This means, for example, there can't be a `#{post-horoscope-status}`. Since they work a bit differently, it is easier for the parser implementation to separate them through different tokens.

I will reinforce that the [source for my blog is available here](https://github.com/vsartor/blog) for authentic and concrete examples :)

#### globals.spec

This file simply defines global variables. So, for example, if you check out my source code you'll see that `https://victhor.io` is not explicitly written on the templates but instead through a global variable called `@{base_url}`.

A further neat little feature I added allows variables to optionally have both a "debugging" and a "production" value. This means that when I build the website, I can pass or not a "production" flag to the generator, which will indicate which of the two values the variable will have. I specify `@{base_url}` in my globals.spec as follows:

```
base_url: /Users/victhor/Blog/output
  prod: https://victhor.io
```

When debugging, the "base URL" will point to my local folder where I build the website so that I can open it locally on my browser and debug it nicely. When building with the "production" flag it will actually point to `https://victhor.io`, which is the version you're consuming right now.

#### pages.spec

We have discussed how some templates specify how to build the homepage or post pages. I also mentioned page-specific variables. `pages.spec` is the file where we specify to the generator what pages need to be built, including the posts I want to be compiled.

I specify a basic page such as the homepage as follows:

```
[home]
template: home
url: index.html
variables:
  title: Home
```

We simply indicate the template to build it, what URL it will have in the end, and I can further specify page-specific variables. Here, I specify the `Home` value for the `title` variable so that when building the home template, any mentions of `@{title}` will be substituted by `Home`.

We require a bit more information for posts, as I've already spoiled. Let's look at the specification of this post as an example:

```
[gochs]
title: My static website generator
date: 2022-10-23
author: Victhor
content: gochs.md
url: gochs.html
template: post
group: posts
variables:
  title: #{post-title}
```

It's different, but it should still be self-explanatory.

You may also ask why using this custom "spec" file format instead of something like JSON or YAML. Well, I wanted to build my own file format and my own parsers for them. Why? [Because why not](https://justforfunnoreally.dev/) ¯\_(ツ)_/¯

#### content, preview, and line

These folders contain the markdown files for the post.

The actual content of the blog post (what you're reading right now) is placed in the content folder.

However, we want a summary of the content when listing the files on the [homepage](@{base_url}) or in the listing pages ([click here for an example](@{base_url}/posts.html)).

We can place short previews of the content (also as a markdown file of the same name) on the `preview` folder and a super brief description of the post on the `line` folder (again, as a markdown file of the same name).

Through the "content" specification on `pages.spec` for each post, the generator will know which markdown files to read and parse for each post!

#### static

Finally, there is the `static` folder.

This folder is a bit boring: every file inside is simply copied to the website folder, without anything interesting happening to it.

This is useful when I want to host images, for example. If I add a image named `image.jpg` in this folder and generate my website, the image will be available on `https://victhor.io/image.jpg`.

#### That's all, folks!

This was the overview of how things work.

For the n-th time, you can check out [the source for my blog here](https://github.com/vsartor/blog).

Alternatively, if you're curious about how I implemented `gochs`, you can also [check out its repository here](https://github.com/vsartor/gochs). It's written in (hopefully understandable) go code!

In case you're curious about the name, I had initially implemented another (but similar) version of the static website generator in Python called ochs, [after the owner of the NYT](https://en.wikipedia.org/wiki/Adolph_Ochs) that grew it into today's fame. Since I eventually migrated to go, calling it `gochs` felt appropriate.

PS: I know I'm bad at naming things. You don't need to tell me.
