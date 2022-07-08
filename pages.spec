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

[essays]
template: list
url: essays.html
variables:
  title: Essays
  group: essays

[whoisvicthor]
title: Who am I?
date: 2022-05-21
author: Victhor Sartório
content: whoisvicthor.md
url: whoisvicthor.html
template: post
unlisted: true
variables:
  title: #{post-title}

[alphanote]
title: The first note
date: 2077-07-28
author: Vitin
content: betanote.md
url: alphanote.html
template: post
group: notes
variables:
  title: #{post-title}

[betanote]
title: The second note
date: 2090-07-28
author: Vitin
content: betanote.md
url: betanote.html
template: post
group: notes
variables:
  title: #{post-title}

[alphapost]
title: The first essay!
date: 2021-05-25
author: Victhor Sartório
content: betanote.md
url: alphapost.html
template: post
group: essays
variables:
  title: #{post-title}

[betapost]
title: The second essay!
date: 2022-05-20
author: Victhor Sartório
content: betanote.md
url: betapost.html
template: post
group: essays
variables:
  title: #{post-title}
