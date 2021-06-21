% rebase('layout.tpl', title=title, year=year)
%import json

<div class="jumbotron">
    <h2>{{ 'Hi there!' }}</h2>
    <h3>{{ 'Do you want to see who is active on our website?' }}</h3>
    <img src="static/images/Cakes.jpg" width = "250" height = "250">
        
    <form action="/activeUsers" method="post">
        <p><input type="submit" value="See active users" class="btn-default"></p>
    </form>
    
    <style>
    .jumbotron{
        background-color: #FFCC33  
    }
    </style>
</div>
