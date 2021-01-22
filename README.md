# Blood-Donation

<h3 class="display-5">Objective of Project:</h3>
      <ul>
        <li>Provide a Basic Information about blood donation.</li>
        <li>Collect the basic information of the donors and also about blood and store it in the database.</li>
        <li>Giving the option to search by location to know the information of the donors in blood bank</li>
        <li>To get to know the how much quantity of blood is present in Blood Bank.</li>
        <li>To provide the information to the acceptor that if blood is not present in the given location then where can he/she can get the required blood.</li>
        <li>Creating Friendly user interface so that any body can handle the website.</li>
        <li>Collecting the basic information of the Acceptor person.</li>
        <li>Instantly deleting the information from blood bank about Blood which the Acceptor collects from blood bank.</li>
      </ul>

Install the all the pacckages in the requirments.txt by command <br>
'pip install -r requirments.txt' <br><br>

This Project is made to run completely on local computer ie local host to run the program in your computer the following modifications has to be made <br>
In My_Sql_data.py file at line number 5
self.con=connector.connect(host='localhost',port=your_mysql_port_number,user='Your_username',password='Your Password',database='database name')<br>
In my case it looks like
self.con=connector.connect(host='localhost',port=3306,user='root',password='Manju@123',database='blood_donation')<br><br>
This Project is made completely from scrath using technologies like Flask,Html,Css,Java and some other module for my academic purpose.<br>
Please contribute to it if any new modification has to be made. Thak you <br>
After making the above changes you can run main.py and can play with it.<br>
For more reference Please go through Project report.
