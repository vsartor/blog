[home]
template: home
url: index.html
variables:
  title: Home

[social]
template: social
url: social.html
variables:
  title: Social

[notes]
template: list
url: notes.html
variables:
  title: Notes
  group: notes

[posts]
template: list
url: posts.html
variables:
  title: Posts
  group: posts

[whoisvicthor]
title: Who am I?
date: 2023-08-13
author: Victhor Sartório
content: whoisvicthor.md
url: whoisvicthor.html
template: post
unlisted: true
variables:
  title: #{post-title}

[note_on_notes]
title: A note on notes
date: 2022-10-23
author: Victhor
content: note_on_notes.md
url: notes.html
template: post
group: notes
variables:
  title: #{post-title}

[gochs]
title: My static website generator
date: 2022-10-24
author: Victhor
content: gochs.md
url: gochs.html
template: post
group: posts
variables:
  title: #{post-title}

[a_bad_post]
title: Alas, a (bad) post
date: 2023-01-29
author: Victhor
content: a_bad_post.md
url: bad_post.html
template: post
group: posts
variables:
  title: #{post-title}

[294_days_later]
title: 294 days later
date: 2023-08-13
author: Victhor
content: 294_days_later.md
url: 294_days_later.html
template: post
group: notes
variables:
  title: #{post-title}

[toylist]
template: toy_list
url: toys.html
variables:
  title: Toys

[betacomparisontoy]
template: betacomparisontoy
url: betacomparisontoy.html
variables:
  title: Beta Comparison Toy

[ihavetoysnow]
title: I have toys now!
date: 2023-08-27
author: Victhor
content: ihavetoysnow.md
url: ihavetoysnow.html
template: post
group: notes
variables:
  title: #{post-title}
