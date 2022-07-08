<p>You are developing an alarm clock app that works as follows: the user can set a date and a time, and the app will ring every week at the given time, starting at the given date until the end of the current year.</p>
<p>The starting date is the only record in the <strong>userInput</strong> table, which has the following structure:</p>
<ul>
<li><code>input_date</code>: the date and time of the first alarm (of a <code>DATETIME</code> type).</li>
</ul>
<p>Given the table, your task is to write a select statement which returns a single column <code>alarm_date</code>. This column should contain all dates (including the time) when the alarm clock will ring. The entries should be arranged in <em>ascending</em> chronological order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>userInput</strong></p>
<table>
<tr>
<th>input_date</th>
</tr>
<tr>
<td>2016-10-23 22:00:00</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>alarm_date</th>
</tr><tr>
  <td>2016-10-23 22:00:00</td>
</tr>
<tr>
  <td>2016-10-30 22:00:00</td>
</tr>
<tr>
  <td>2016-11-06 22:00:00</td>
</tr>
<tr>
  <td>2016-11-13 22:00:00</td>
</tr>
<tr>
  <td>2016-11-20 22:00:00</td>
</tr>
<tr>
  <td>2016-11-27 22:00:00</td>
</tr>
<tr>
  <td>2016-12-04 22:00:00</td>
</tr>
<tr>
  <td>2016-12-11 22:00:00</td>
</tr>
<tr>
  <td>2016-12-18 22:00:00</td>
</tr>
<tr>
  <td>2016-12-25 22:00:00</td>
</tr>
</table>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/alarmClocks/img/example.jpg?_tm=1611831908282" alt="example" /></p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
