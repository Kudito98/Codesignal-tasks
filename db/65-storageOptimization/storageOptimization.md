<p>You noticed that your server is running out of free HDD space. You investigated and discovered that most of the space is taken up by the <strong>workers_info</strong> table, which has the following structure:</p>
<ul>
<li><code>id</code>: the unique worker ID;</li>
<li><code>name</code>: the name of the worker;</li>
<li><code>date_of_birth</code>: the worker's date of birth;</li>
<li><code>salary</code>: the worker's salary.</li>
</ul>
<p>One strange thing about this table is that a lot of its rows contain <code>NULL</code> values in some of the columns (except for the <code>id</code> column, which always contains a non-NULL value).</p>
<p>After thinking about this problem, you've decided to change the way you store data in <strong>workers_info</strong>. Instead of keeping the cells with <code>NULL</code> values in the table, you will only store <code>id</code>, <code>column_name</code>, and <code>value</code> columns. <code>column_name</code> will contain the name of a column that contains a non-NULL value for each <code>id</code>. <code>value</code> will be the value from this row, converted to a string. For dates, use the format <code>YYYY-MM-DD</code>.</p>
<p>Given the <strong>workers_info</strong> table, your task is to write a select statement which returns the following three columns: <code>id</code>, <code>column_name</code>, and <code>value</code>, that contain the workers' <code>id</code>s, the column names, and the stringified values, in the format described above. The output should be sorted in ascending order by <code>id</code>. Rows with the same <code>id</code> should be sorted by column names in the following order: <code>name</code>, <code>date_of_birth</code>, and then <code>salary</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>workers_info</strong>, where empty cells stand for a <code>NULL</code> value</p>
<table><tr><th>id</th><th>name</th><th>date_of_birth</th><th>salary</th></tr>
<tr>
  <td>1</td>
  <td>Justin Penrose</td>
  <td>1969-03-01</td>
  <td>3000</td>
</tr>
<tr>
  <td>2</td>
  <td></td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>3</td>
  <td>Robt Claire</td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>10</td>
  <td></td>
  <td>1970-12-12</td>
  <td></td>
</tr>
<tr>
  <td>11</td>
  <td></td>
  <td></td>
  <td>5000</td>
</tr>
<tr>
  <td>12</td>
  <td>Yuk Kluge</td>
  <td></td>
  <td>4500</td>
</tr>
</table>
<p>the output should be</p>
<table><tr><th>id</th><th>column_name</th><th>value</th></tr>
<tr>
  <td>1</td>
  <td>name</td>
  <td>Justin Penrose</td>
</tr>
<tr>
  <td>1</td>
  <td>date_of_birth</td>
  <td>1969-03-01</td>
</tr>
<tr>
  <td>1</td>
  <td>salary</td>
  <td>3000</td>
</tr>
<tr>
  <td>3</td>
  <td>name</td>
  <td>Robt Claire</td>
</tr>
<tr>
  <td>10</td>
  <td>date_of_birth</td>
  <td>1970-12-12</td>
</tr>
<tr>
  <td>11</td>
  <td>salary</td>
  <td>5000</td>
</tr>
<tr>
  <td>12</td>
  <td>name</td>
  <td>Yuk Kluge</td>
</tr>
<tr>
  <td>12</td>
  <td>salary</td>
  <td>4500</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
