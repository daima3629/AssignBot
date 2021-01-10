# AssignBot

### Description
あるBot開発者が集まるDiscordサーバーでのこと。  
一つの質問に対して、たくさんのユーザーが回答し、質問した人が困惑する場面が多くありました。  
由々しき問題だと思ったので、なんとかして「質問者:回答者=1:2」ぐらいに制限できるシステムを作れないかと、そう考えた結果このBotができました。

### Features
- `a.open`  
issueを開きます。このコマンドを打ったあとに質問をしてくだだい。
- `a.assign`  
開かれたissueに対してassign(回答者として参加)します。  
このときに3人以上assignをすると警告を表示します。
- `a.close`  
開かれたissueを閉じます。

### author
- **daima3629#1235**

### LICENSE
このBotにはMITライセンスが採用されています。  
全文は[こちら](https://github.com/daima3629/AssignBot/blob/master/LICENSE)です。

### How to invite
[こちら](https://discord.com/api/oauth2/authorize?client_id=797721278797709312&permissions=84992&scope=bot)からBotを招待できます。  
必要権限は

- `View Channels`
- `Send Mesages`
- `Embed Links`
- `Read Mesage History`

の4つです。
