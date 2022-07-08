<p>You need to connect to a remote database and extract some information from it. The problem is, you don't know the name of the most important table in this database! You were told that it should start with the letter <code>e</code> and end with the letter <code>s</code>. Now you want to find all possible candidates, i. e. tables with such names, as well as their column names and their datatypes. It is guaranteed that at least one such table exists in the database.</p>
<p>You have already connected to the database named <code>ri_db</code>. Now you just need to implement a procedure that will find the information about the most important table in it, as described above. The resulting table should have the following structure:</p>
<ul>
<li><code>tab_name</code>: the name of the found table;</li>
<li><code>col_name</code>: the name of the column in the found table;</li>
<li><code>data_type</code>: the type of this column.</li>
</ul>
<p>The rows in the output should be sorted first by the name of the table, then by the column names.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>events</strong></p>
<table>
  <tr>
    <th>event_date</th>
    <th>event_name</th>
  </tr>
  <tr>
    <td>2016-10-08</td>
    <td>Mum's birthday</td>
  </tr>
  <tr>
    <td>2016-10-31</td>
    <td>Halloween</td>
  </tr>
</table>
<p>and <strong>guestlist</strong> in the database</p>
<table>
  <tr>
    <th>id</th>
    <th>first_name</th>
    <th>surname</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John</td>
    <td>Miller</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Evelyn</td>
    <td>Ross</td>
  </tr>
</table>
<p>the output should be</p>
<table>
  <tr>
    <th>tab_name</th>
    <th>col_name</th>
    <th>data_type</th>
  </tr>
  <tr>
    <td>events</td>
    <td>event_date</td>
    <td>date</td>
  </tr>
  <tr>
    <td>events</td>
    <td>event_name</td>
    <td>varchar</td>
  </tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
