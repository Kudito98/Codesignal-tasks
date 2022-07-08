<p>You recently added feedback functionality to the small web service you own. You were able to handle everything manually at first, but the amount of messages you receive now is overwhelming. As such, you've decided to start generating generic responses automatically.</p>
<p>All customer names are stored in the table <strong>customers</strong> with the following structure:</p>
<ul>
<li><code>id</code>: unique customer id;</li>
<li><code>name</code>: the name of the customer in the format described below.</li>
</ul>
<p>The customer's <code>name</code> is stored in the following format: <code>&lt;first name&gt; &lt;last name&gt;</code> (two words separated by single space), where first and last names can contain both uppercase and lowercase English letters.</p>
<p>Your task is to write a function that, given the customer's <code>name</code>, will return the following message:</p>
<p><code>Dear &lt;Firstname&gt; &lt;Lastname&gt;! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.</code></p>
<p>Here, <code>&lt;Firstname&gt;</code> and <code>&lt;Lastname&gt;</code> are the first and the last names of the customer, with the first letter in uppercase and with all other letters in lowercase.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>customers</strong></p>
<table>
<tr>
<th>id</th>
<th>name</th>
</tr>
<tr>
<td>1</td>
<td>JOHN GaLT</td>
</tr>
<tr>
<td>2</td>
<td>SANDY COHEN</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>name</th>
<th>response</th>
</tr>
<tr>
<td>1</td>
<td>JOHN GaLT</td>
<td>Dear John Galt! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.</td>
</tr>
<tr>
<td>2</td>
<td>SANDY COHEN</td>
<td>Dear Sandy Cohen! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
