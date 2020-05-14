<p>
  The project is an implementation of the article: The Password Reset MitM Attack.<br>
  <a href="https://www.ieee-security.org/TC/SP2017/papers/207.pdf">paper link</a> <br>
  A sequence diagram that describes the attack:
<img src="https://www.bleepstatic.com/images/news/u/986406/Research/PRMitM.png" height="400" width="800"> <br>
</p>

-The user registers to the site <br>
-He recieves a sms with authorization code <br>
-He inserts the code to the form <br>
-His Facebook password is changed.

<p>
<h5>Assumption:</h5>
There is exactly one Facebook account related to the inserted phone number. (Facebook allows the same phone number to be related to more than one account) <br>
We could reset the user's password with the email  address in the same fashion (In Facebook each account has a unique email address).
</p>

<p>
  As one can notice, the SMS message contains the words "Your Facebook password reset code is ...".
  This can immediately cause the user to suspect because he didn't have any interaction with Facebook. <br>
  One possible solution is to intercept the sms and steal the code, thus taking his password before he realizes he has been cheated. <br>
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
