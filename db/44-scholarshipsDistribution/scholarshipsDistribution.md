<p>In the past, straight "A" students have gotten scholarships to reward them for their excellent grades. This year, though, there has been an increase in the number of detentions given to excellent students, so the administration is going to change the rules. In order to encourage the levels of misbehavior to go down, only well-behaved students will be awarded with scholarships this year.</p>
<p>Information about the straight "A" students is stored in the table <strong>candidates</strong>, and information about all the detentions is stored in the table <strong>detentions</strong>. Here are their structures:</p>
<ul>
<li><strong>candidates</strong>
<ul>
<li><code>candidate_id</code>: the unique candidate ID;</li>
<li><code>candidate_name</code>: the name of the candidate;</li>
</ul>
</li>
<li><strong>detentions</strong>
<ul>
<li><code>detention_date</code>: the date of the detention (of the <code>date</code> type);</li>
<li><code>student_id</code>: the id of the student who got the detention.</li>
</ul>
</li>
</ul>
<p>Your task is to figure out which students should get the scholarships this year. Given the <strong>candidates</strong> and <strong>detentions</strong> tables, return a table with a single <code>student_id</code> column containing the IDs of the students who should get scholarships - students from the <strong>candidates</strong> table who've never gotten a detention. The IDs of the students in the resulting table should be sorted in ascending order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>candidates</strong></p>
<table>
<tr>
<th>candidate_id</th>
<th>candidate_name</th>
</tr>
<tr>
<td>12</td>
<td>Gerlinde Addens</td>
</tr>
<tr>
<td>35</td>
<td>Gerbern Abbey</td>
</tr>
<tr>
<td>44</td>
<td>Edmond Ramsay</td>
</tr>
<tr>
<td>58</td>
<td>Svanhild Lacey</td>
</tr>
<tr>
<td>103</td>
<td>Nita Simons</td>
</tr>
</table>
<p>and <b>detentions</b></p>
<table>
<tr>
<th>detention_date</th>
<th>student_id</th>
</tr>
<tr>
<td>2015-10-21</td>
<td>12</td>
</tr>
<tr>
<td>2015-11-19</td>
<td>91</td>
</tr>
<tr>
<td>2016-02-11</td>
<td>87</td>
</tr>
<tr>
<td>2015-12-26</td>
<td>44</td>
</tr>
<tr>
<td>2016-01-19</td>
<td>91</td>
</tr>
<tr>
<td>2015-09-10</td>
<td>91</td>
</tr>
<tr>
<td>2015-12-30</td>
<td>12</td>
</tr>
<tr>
<td>2016-05-19</td>
<td>58</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>student_id</th>
</tr>
<tr>
<td>35</td>
</tr>
<tr>
<td>103</td>
</tr>
</table>
<p>Only Gerbern Abbey and Nita Simons never got detention, so they will get the scholarships this year.</p>
<p>The dates in the example are given in the <code>YYYY-MM-DD</code> format.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
