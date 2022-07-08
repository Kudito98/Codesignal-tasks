<p>The company you work for has a database with the IP addresses of all the company's computers in it. When a new computer is purchased, an employee adds its <a href="keyword://ipv4-address" target="_blank">IPv4 address</a> to this database. Unfortunately, you've just discovered that there is no address validation, so some of the records are incorrect.</p>
<p>Now your boss wants you to write a program that will find and retain only the correct records from this table. A record is correct if the IP it contains is a valid IPv4 address, and either the first or the second component in the <strong>host part</strong> is a two-digit number.</p>
<p>The <strong>ips</strong> table contains the following columns:</p>
<ul>
<li><code>id</code>: the unique ID of the computer;</li>
<li><code>ip</code>: the unique IP address of the computer.</li>
</ul>
<p>Your task is to write a select statement which returns only the correct records from the given <strong>ips</strong> table. This table should be sorted by <code>id</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the given table <strong>ips</strong></p>
<table>
<tr>
<th>id</th>
<th>ip</th>
</tr>
<tr>
<td>4</td>
<td>"1.1.1.1"</td>
</tr>
<tr>
<td>3</td>
<td>"1.111.111.11"</td>
</tr>
<tr>
<td>2</td>
<td>"11.11.11.11"</td>
</tr>
<tr>
<td>1</td>
<td>"11.11.11.11.11.11"</td>
</tr>
<tr>
<td>5</td>
<td>"11.11.11.111"</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>ip</th>
</tr>
<tr>
<td>2</td>
<td>"11.11.11.11"</td>
</tr>
<tr>
<td>3</td>
<td>"1.111.111.11"</td>
</tr>
<tr>
<td>5</td>
<td>"11.11.11.111"</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
