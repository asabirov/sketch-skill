# Pattern library

The library has 76 patterns in 9 categories. A category is a product area. Each pattern folder holds `pattern.md`, `transitions.json` and `sketch.html`.

Start a sketch from the `sketch.html` of a pattern whose "Best for" line fits the screen. A pattern value is a proposal to the designer, not a design-system token.

## account

| Pattern | Best for |
| --- | --- |
| [`account/connected-apps`](../library/account/connected-apps/) | A signed-in reader sees each outside app that uses their account, with its access, the connect date and the last use, and disconnects one app after a confirmation. For a short list of the clients of a workspace inside a settings window, use `account/oauth-consent`. |
| [`account/email-code-signup`](../library/account/email-code-signup/) | The sign-up of a work tool that signs in with an emailed code, creates a workspace, and then runs a short paged onboarding. Use it for a passwordless sign-in, a "building your workspace" wait, and a 5-step setup pager with skip on each step. |
| [`account/live-preview-signup`](../library/account/live-preview-signup/) | The sign-up of a team product, where each answer can show its result at once. Use it when a new team names its workspace, says what it uses the product for, and takes its first steps in the app. |
| [`account/oauth-consent`](../library/account/oauth-consent/) | A person lets an outside app act for their account, and later takes that right back in Settings. |
| [`account/waitlist`](../library/account/waitlist/) | A person asks for access to a new service and needs a clear result. |

## analytics

| Pattern | Best for |
| --- | --- |
| [`analytics/account-list`](../library/analytics/account-list/) | A card on an overview page that compares the money in a few accounts, pots or wallets, and opens one of them. |
| [`analytics/action-row`](../library/analytics/action-row/) | The top of an overview page, where a person starts the most common jobs of the product without a menu. |
| [`analytics/balance-card`](../library/analytics/balance-card/) | A person opens a money product to see how much money the business has now, and how the total moved over a period that they choose. |
| [`analytics/range-brush`](../library/analytics/range-brush/) | Any chart over time where a person sets the shown range by a drag, and needs to see where that range sits in the whole time. |
| [`analytics/summary-card`](../library/analytics/summary-card/) | A small card on an overview page that answers one question about one part of the product, such as "how much of the limit is used" or "how many bills are late", and links to the full page. |

## chat

| Pattern | Best for |
| --- | --- |
| [`chat/app-in-a-chat`](../library/chat/app-in-a-chat/) | An assistant that puts a small working app into a conversation. Use it when a person does a short task in an app without leaving the chat, and a longer task needs the whole screen. |
| [`chat/avatar-badges`](../library/chat/avatar-badges/) | A chat product where a person sees at a glance which chat is the main one and which chats have new messages. |
| [`chat/avatar-badges-counts`](../library/chat/avatar-badges-counts/) | A chat product where the number of new messages changes what the person opens first, such as a support inbox. |
| [`chat/avatar-badges-row-end`](../library/chat/avatar-badges-row-end/) | A chat product with small avatars, or with rows that have no avatar, where a person sees which chats have new messages. |
| [`chat/channel-thread-panel`](../library/chat/channel-thread-panel/) | A team chat with busy channels, where a person sees which message has a thread, reads its last reply without leaving the channel, and reads and answers the thread while the channel keeps its place. |
| [`chat/chat-list`](../library/chat/chat-list/) | A phone app where a person picks one chat from all their chats, or finds a chat by its text. |
| [`chat/chat-list-filter-in-place`](../library/chat/chat-list-filter-in-place/) | A phone app with a short list of chats, where a search finds only chats. |
| [`chat/chat-list-tab-bar`](../library/chat/chat-list-tab-bar/) | A phone app with 3 to 5 sections that a person changes between many times a day. One section is the list of chats. |
| [`chat/conversation-pane`](../library/chat/conversation-pane/) | A chat app where one-to-one and small group conversations get their own page. Use it for a list of conversations beside the open conversation, with a reading pane and a composer. |
| [`chat/create-a-chat`](../library/chat/create-a-chat/) | A phone app where a person makes a new chat and gives it an avatar that tells it apart from the other chats. |
| [`chat/create-a-chat-initials`](../library/chat/create-a-chat-initials/) | A phone app with many chats that a person knows by name, where a new chat needs only a name and a colour. |
| [`chat/create-a-chat-picture`](../library/chat/create-a-chat-picture/) | A phone app where a chat stands for a real person, place or thing, and a picture tells it apart from the other chats. |
| [`chat/voice-message`](../library/chat/voice-message/) | A chat where a person listens to a spoken message, and records one in place of text. |
| [`chat/voice-message-hold-to-record`](../library/chat/voice-message-hold-to-record/) | A chat where spoken messages are short and frequent, and a person records one with one hold of a button. |
| [`chat/voice-message-transcript`](../library/chat/voice-message-transcript/) | A chat where a person cannot listen, or looks for a spoken message by its words. |

## content

| Pattern | Best for |
| --- | --- |
| [`content/card-strips`](../library/content/card-strips/) | A team product where a member wants a look at each group of records before a choice. |
| [`content/catalog-base-view`](../library/content/catalog-base-view/) | A product with one set of records that people scan by picture, compare by field and follow by status. |
| [`content/catalog-display-panel`](../library/content/catalog-display-panel/) | A product with one set of records that people scan by picture, compare by field and follow by status. |
| [`content/catalog-side-list`](../library/content/catalog-side-list/) | A product with one set of records that people scan by picture, compare by field and follow by status. |
| [`content/catalog-tabs`](../library/content/catalog-tabs/) | A product with one set of records that people scan by picture, compare by field and follow by status. |
| [`content/comment-thread`](../library/content/comment-thread/) | A product where members discuss one post. A reader follows each line of talk, answers in the right place and reacts without a new comment. |
| [`content/comment-tree`](../library/content/comment-tree/) | A product where many members answer one post, and an answer gets its own answers. A reader follows one branch and closes a branch that does not help. |
| [`content/compact-feed`](../library/content/compact-feed/) | A product where groups post updates, and a member keeps up with them in one stream. The member reads each post in full and answers without leaving the stream. |
| [`content/document-match`](../library/content/document-match/) | A finance product where a person matches a bank transaction with an invoice, and checks the data read from the invoice against the document, one decision at a time. |
| [`content/fact-cards`](../library/content/fact-cards/) | A team product where a member scans many records by their main numbers, and then opens one record. |
| [`content/feed-full-posts`](../library/content/feed-full-posts/) | A product where groups post updates, and a member keeps up with them in one stream. The member reads each post in full and answers without leaving the stream. |
| [`content/feed-short-posts`](../library/content/feed-short-posts/) | A product where members post short messages many times a day and the feed has no end. A member sees what happens now and decides on each post in a few seconds. |
| [`content/feed-topic-cards`](../library/content/feed-topic-cards/) | A product where each post starts a discussion that members come back to. A member finds a discussion or starts one. |
| [`content/forum-list`](../library/content/forum-list/) | A product where each post starts a discussion that members come back to. A member finds a discussion or starts one. |
| [`content/kanban`](../library/content/kanban/) | A team product where a member compares the groups of its records, such as the stages, and then opens one record. |
| [`content/leaderboard`](../library/content/leaderboard/) | A team product where a member compares many records by their rank in one number, and then opens one record. |
| [`content/marketplace`](../library/content/marketplace/) | A person looks for an add-on for a product, searches and filters a large catalog, reads about one item and adds it to their account. |
| [`content/product-page`](../library/content/product-page/) | A team product where a member reads the main numbers of one record, then the course of one number, and then the facts. |
| [`content/ranked-groups`](../library/content/ranked-groups/) | A team product where a member compares groups of records by one number first, and then wants the best records of each group. |
| [`content/sort-heads`](../library/content/sort-heads/) | A team product where a member compares 2 or more numbers of many records at the same time, and then opens one record. |
| [`content/timeline`](../library/content/timeline/) | A product where members post short messages many times a day and the feed has no end. A member sees what happens now and decides on each post in a few seconds. |
| [`content/wide-grid`](../library/content/wide-grid/) | A team product where a member chooses one group of records, and then scans all records of that group. |

## navigation

| Pattern | Best for |
| --- | --- |
| [`navigation/foot-menu`](../library/navigation/foot-menu/) | A team product where a signed-in member checks which account is signed in, then reaches their settings and the way out. |
| [`navigation/swipe-back`](../library/navigation/swipe-back/) | A phone app where a person goes into a record and comes back with one thumb, without a reach to the top of the screen. |
| [`navigation/swipe-back-full-width`](../library/navigation/swipe-back-full-width/) | A phone app where a person comes back from a record with one thumb, and the page has no part that takes a sideways swipe. |
| [`navigation/swipe-back-labelled`](../library/navigation/swipe-back-labelled/) | A phone app where a page opens from more than one screen, and the person must know where Back goes. |
| [`navigation/topics-tree`](../library/navigation/topics-tree/) | A chat product that sorts the messages of a channel into topics, where a person goes to one topic of one channel. |
| [`navigation/topics-tree-collapsible`](../library/navigation/topics-tree-collapsible/) | A chat product where a person is in many channels, or a channel has many topics, and goes to one topic of one channel. |
| [`navigation/topics-tree-side-pane`](../library/navigation/topics-tree-side-pane/) | A chat product on a screen from 600 px wide, where a person changes between topics and keeps the tree in view. |
| [`navigation/user-menu`](../library/navigation/user-menu/) | A team product where a signed-in member reaches their own account: who is signed in, their settings and the way out. |

## notifications

| Pattern | Best for |
| --- | --- |
| [`notifications/activity-feed`](../library/notifications/activity-feed/) | A chat app where mentions, replies, reactions and app messages from many channels come to one list. Use it for an activity page in an app rail, with tabs for saved views, a filter popover, and bulk triage. |
| [`notifications/follow-menu`](../library/notifications/follow-menu/) | A product where a member follows a product, a topic or a person with one button, and sets how many alerts come. |
| [`notifications/inbox-popover`](../library/notifications/inbox-popover/) | A community chat where unread messages from many channels and servers come to one popover, grouped by channel. Use it for an inbox that opens over the open channel from an icon button, with tabs for unreads and mentions. |
| [`notifications/notification-inbox`](../library/notifications/notification-inbox/) | A work tool where a notification points at a record to act on, and a person works through many in one sitting. Use it when a person sorts notifications by need and acts on each one. |
| [`notifications/subscribe-popover`](../library/notifications/subscribe-popover/) | A product that a person follows with no account. The person chooses where the alerts go: an email address, a phone number or a feed reader. |

## profile

| Pattern | Best for |
| --- | --- |
| [`profile/character-builder`](../library/profile/character-builder/) | A mobile character or avatar builder where the user picks parts and sees the result at once, then saves to a profile. Use it for a profile avatar maker or a game character maker. |
| [`profile/member-profile`](../library/profile/member-profile/) | A product where each member has a public page. A visitor decides who a member is, reads what the member posted and goes to the pages of the member on other sites. |
| [`profile/portfolio-profile`](../library/profile/portfolio-profile/) | A product where the value of a member is the work that the member published. A visitor finds the work of a member and decides whether to follow or hire the member. |
| [`profile/profile-card`](../library/profile/profile-card/) | A product where members meet in a conversation. A visitor needs a short answer to "who is this" and then continues the conversation. |

## settings

| Pattern | Best for |
| --- | --- |
| [`settings/settings`](../library/settings/settings/) | A desktop work app with many groups of settings, where a person leaves the work for a time to find, change and check settings, then goes back to the work. |
| [`settings/members-list`](../library/settings/members-list/) | A person who manages a shared account, such as a family or a small team, sees each member with a role and the last activity, invites a member with a role, decides on a request to join, and signs a member out of one device or of all devices. For the profile that other members see, use `profile/member-profile`. |
| [`settings/notification-settings-by-channel`](../library/settings/notification-settings-by-channel/) | A product that sends events on more than one channel and has more than 15 kinds of event. A member chooses which events notify them on each channel, and turns a channel off without losing the choices for its events. |
| [`settings/notification-settings-by-event`](../library/settings/notification-settings-by-event/) | A product that sends fewer than 13 kinds of event on 2 or 3 channels. A member chooses how each kind of event reaches them, and from whom. |
| [`settings/settings-modal`](../library/settings/settings-modal/) | A product with more than 4 groups of settings, where a person finds one setting of their account or of a shared workspace. |
| [`settings/theme-switch-preview-cards`](../library/settings/theme-switch-preview-cards/) | A signed-in reader chooses how the product looks in a section of its own, and sees a small picture of each choice before choosing. The choice applies at once, with no Save button. For a product that has the look only as a short choice in its account menu, use the theme submenu of `navigation/user-menu`. |

## sheets

| Pattern | Best for |
| --- | --- |
| [`sheets/bottom-sheet`](../library/sheets/bottom-sheet/) | A phone app shows a short set of choices over the screen, and the person goes back to the screen with one move. |
| [`sheets/bottom-sheet-peek`](../library/sheets/bottom-sheet-peek/) | A phone app where a person works with the screen and a sheet together, such as a map with a list of places. |
| [`sheets/bottom-sheet-two-heights`](../library/sheets/bottom-sheet-two-heights/) | A phone app shows a long list over the screen, and the person must still see the screen behind it. |
| [`sheets/catalogue-sheet`](../library/sheets/catalogue-sheet/) | A phone app where a person looks through a set of records, makes the set smaller, and does one action on a record. |
| [`sheets/catalogue-sheet-multi-select`](../library/sheets/catalogue-sheet-multi-select/) | A phone app where a person does one action on many records of a set, such as an invitation to a group. |
| [`sheets/catalogue-sheet-search-top`](../library/sheets/catalogue-sheet-search-top/) | A phone app where a person starts each visit to a set of records with a search, then does one action on a record. |
