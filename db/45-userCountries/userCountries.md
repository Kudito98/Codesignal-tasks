<p>You are really interested in statistics, and your new project is to gather some information about the users of a big social network. More specifically, you want to know which countries these users are from. Using the social network's API, you managed to collect enough data to compose two tables <strong>users</strong> and <strong>cities</strong>, which have the following structures:</p>
<ul>
<li><strong>users</strong>:
<ul>
<li><code>id</code>: the unique user ID;</li>
<li><code>city</code>: the name of the city where this user lives;</li>
</ul>
</li>
<li><strong>cities</strong>:
<ul>
<li><code>city</code>: a unique city name;</li>
<li><code>country</code>: the name of the country where this city is located.</li>
</ul>
</li>
</ul>
<p>Given the tables <strong>users</strong> and <strong>cities</strong>, write a select statement that returns two columns <code>id</code> and <code>country</code> consisting of user <code>id</code>s and the countries where they live respectively. If a user's city is missing from the <strong>cities</strong> table, the <code>country</code> column should contain <code>"unknown"</code> instead.</p>
<p>Return the table sorted by users' <code>id</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>users</strong></p>
<table>
  <tr>
    <th>id</th>
    <th>city</th>
  </tr>
  <tr>
    <td>1</td>
    <td>San Francisco</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Moscow</td>
  </tr>
  <tr>
    <td>3</td>
    <td>London</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Washington</td>
  </tr>
  <tr>
    <td>5</td>                
    <td>New York</td>
  </tr>
  <tr>
    <td>6</td>                
    <td>Saint Petersburg</td>
  </tr>
  <tr>
    <td>7</td>                
    <td>Helsinki</td>
  </tr>
</table>
<p>and the following table <strong>cities</strong></p>
<table>
  <tr>
    <th>city</th>
    <th>country</th>
  </tr>
  <tr>
    <td>Moscow</td>
    <td>Russia</td>
  </tr>
  <tr>
    <td>Saint Petersburg</td>
    <td>Russia</td>
  </tr>
  <tr>
    <td>San Francisco</td>
    <td>USA</td>
  </tr>
  <tr>
    <td>Washington</td>
    <td>USA</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>USA</td>
  </tr>
  <tr>
    <td>London</td>
    <td>England</td>
  </tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>country</th>
</tr>
<tr>
<td>1</td>
<td>USA</td>
</tr>
<tr>
<td>2</td>
<td>Russia</td>
</tr>
<tr>
<td>3</td>
<td>England</td>
</tr>
<tr>
<td>4</td>
<td>USA</td>
</tr>
<tr>
<td>5</td>
<td>USA</td>
</tr>
<tr>
<td>6</td>
<td>Russia</td>
</tr>
<tr>
<td>7</td>
<td>unknown</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
