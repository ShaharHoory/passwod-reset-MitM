<p>
  The project is an implementation of the attack presented in <a href="https://www.ieee-security.org/TC/SP2017/papers/207.pdf">this       article.</a> <br>
  A sequence diagram that describes the attack:
<img src="https://www.bleepstatic.com/images/news/u/986406/Research/PRMitM.png" height="400" width="800"> <br>
</p>

-The user registers to the site <br>
-They recieves an sms with authorization code <br>
-They inserts the code to the form <br>
-Their Facebook password will be changed.

<p>
<h5>Assumption:</h5>
There is only one Facebook account relates to the inserted phone number. (Facebook allows the same phone number to be related to more than one account) <br>
Similarly, we could reset the user's password with the email address and not with the phone number (In Facebook each account has a unique email address).
</p>

<p>
  As one can notice, the SMS message contains the words "Your Facebook password reset code is ...".
  This can immediately cause the user to suspect because he didn't have any interaction with Facebook. <br>
  One possible solution is to interept the sms and steal the code, and even bofore the user understands that he has been cheated, change his password. <br>
  We can also notice that the above article's authors claim that most of the users do not read the entire sms but just read the code.
</p>

<p>
  In order to run the project, run 'flaskblog.py'.
  <h4>Required Libraries:</h4>
  <ul>
    <li> Flask </li>
    <li> Selenium </li>
  </ul>
</p>

<p>
  -Shahar Hoory- <br />
  -Dan Gvili- <br>
  2018
</p>
