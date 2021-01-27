wordpress или github pages

[In reply to Mikhail Zybin]
> потому что вконтакте, фейсбук, телеграм и телетайп не рендерят markdown

GitHub сам по себе (даже не GitHub Pages) вполне сносно рендерит GitHub Flavored Markdown. Допускает и дополнительные фишечки разметки типа чекбоксы для task lists.

> Что лучше - создавать блог через wordpress или github.pages?

Имхо, GitHub лучше; но я не готов сейчас это обосновывать. GitHub Pages + static site generator (например, Jekyll) — это следующий шаг, если нужны рюшечки.

Имхо, для упомянутых целей лучше искать платформу не для блога (привязка к дате, поток мимолётных событий, комментарии/ленты/уведомления), а для т.н. digital garden. (Ранее в соседнем чате уже упоминалось со ссылками, можно поискать.)

Возможно, стоит разделить свой writing на два репозитория — публичный (digital garden), чтобы можно было шарить оформленные куски мыслей, их причёсывать и лелеять; и приватный (handbook/personal knowledge base), чтобы можно было писать свободно, быстро и без давления.

https://stackoverflow.com/questions/59096243/adding-comments-in-blog-posts-on-github-pages

https://stackoverflow.com/questions/59096243/adding-comments-in-blog-posts-on-github-pages

You can use GitHub Issues themselves, in a public repo, as a commenting system, via a 3rd-party GitHub plugin called "utterances". See here:

1.  Utterances main page & installation info.: [https://utteranc.es/](https://utteranc.es/)
2.  Utterances GitHub repo: [https://github.com/utterance/utterances](https://github.com/utterance/utterances)
3.  You must install the utterances plugin into your GitHub account, here: [https://github.com/apps/utterances](https://github.com/apps/utterances)
    1.  GitHub lets you install this app for all of your respositories, or just repositories you select, which is nice. You may just want to install it on GitHub Pages repos you have, since it only needs access to those repos.
    2.  Make sure your repos using utterances are _public_, or else readers won't be able to view the issues/comments, or comment.

Other options also exist. [Michael Rose](https://github.com/mmistakes), the creator of the [#1 most popular](https://github.com/topics/jekyll-theme) GitHub-Pages-compatible [minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme (see a [demo here](https://mmistakes.github.io/minimal-mistakes/)), has put together a [short list of **commenting systems** here](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#comments).

1.  [Disqus](https://disqus.com/)
2.  [Discourse](https://www.discourse.org/)
3.  [Facebook](https://developers.facebook.com/docs/plugins/comments)
4.  [utterances](https://utteranc.es/) - my favorite, since it is Free and Open Source ([MIT license](https://github.com/utterance/utterances/blob/master/LICENSE.md)) and no-cost, and uses 1.  convenient GitHub Issues as the commenting system. GitHub Issues comments have _excellent_ markdown support, allow inserting nicely-formatted code blocks right into them, can be edited indefinitely, moderated by you (including editing or deleting comments which are inappropriate), and responded to with upvote buttons--all reasons I like them.
2.  [Staticman](https://staticman.net/)

Update Jan. 2021: I have now implemented Utterances on my personal website here: [https://gabrielstaples.com/](https://gabrielstaples.com/). Example page: [https://gabrielstaples.com/google-pixel2-touchscreen/](https://gabrielstaples.com/google-pixel2-touchscreen/) -- scroll to the bottom to see the Utterances (GitHub Issues-based) comment section.

Что такое gem?
Есть какие-то jekyll-themes.