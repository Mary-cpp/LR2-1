% rebase('layout.tpl', title='Welcome to Bubochnaya family', year=year)

<div class="jumbotron">
     <p algin = "right" hspace = "right">"The only thing missing in cooking is your appetite."</p>
    <h1>About us</h1>
    <img src="static/images/Cinnabons.jpg">
    <p class="lead">
    <p align="left">We work with the highest quality raw materials, without dyes and preservatives! Our bakery and confectionery products are handmade. In our assortment you can find legendary and all your favorite cakes such as potato cake, eclairs, count ruins, honey cake, classic sour cream cake and much more! 
    <style>
    .jumbotron{
        background-color: #FFCC33  
    }
    </style>
        <h3> Ask a Question </h3>
        <form action="/home" method="post">
            <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
            <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
            <p><input type="submit" value="Send"></p>
         </form>

</div>

<div class="row">

    <div class="col-md-4">
       <h2>Best employees</h2>
        <p>
            Our young qualified and friendly team is happy to help you enjoy the products from our menu. If you want to join us, click here (^_^)
        </p>
    </div>
    <div class="col-md-4">
        <h2>Fresh pastry</h2>
        <p>
            Every morning we bake fresh bread to treat our visitors. Come and see what's new on our menu
        </p>
        <p><a class="btn btn-default" href="https://docs.google.com/spreadsheets/d/1_IAOobNhaUuAG5kovriPIPFrwSvmI8VCq3-9J0_URpw/edit#gid=731215286">Menu &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Service</h2>
        <p> 
            You can enjoy sincerity and opennes of our perconal. 
        </p>
    <style>
        .row{
            background-color: #FFCC33  
        }
    </div>
</div>



