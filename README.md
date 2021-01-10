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
