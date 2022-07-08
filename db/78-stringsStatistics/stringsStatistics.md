<p>You are collecting some statistics about strings in the table <strong>strs</strong>, which only has one column:</p>
<ul>
<li><code>str</code> - a unique string that consists only of lowercase English letters.<br />
Your goal is to return a new table <strong>ans</strong>, which has the following columns:</li>
<li><code>letter</code> - a unique lowercase English letter;</li>
<li><code>total</code> - the total number of occurrences of this letter in all the strings from table <strong>strs</strong>;</li>
<li><code>occurrence</code> - the number of strings from table <strong>strs</strong> in which this letter occurs at least once;</li>
<li><code>max_occurrence</code> - the maximal number of occurrences of this letter in a single string;</li>
<li><code>max_occurence_reached</code> - the number of strings in which this maxumal number of occurrences is reached.</li>
</ul>
<p>The rows should be ordered lexicographically by <code>letter</code>. For letters that are not contained in the <strong>strs</strong> table, don't add a row to the output table (i.e., all integers in the <code>total</code> column should be positive).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For given table <strong>strs</strong></p>
<table>
<tr>
<th>str</th>
</tr>
<tr>
<td>aa</td>
</tr>
<tr>
<td>aaaa</td>
</tr>
<tr>
<td>aab</td>
</tr>
<tr>
<td>abaaba</td>
</tr>
<tr>
<td>bbbbb</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>letter</th>
<th>total</th>
<th>occurrence</th>
<th>max_occurrence</th>
<th>max_occurrence_reached</th>
</tr>
<tr>
<td>a</td>
<td>12</td>
<td>4</td>
<td>4</td>
<td>2</td>
</tr>
<tr>
<td>b</td>
<td>8</td>
<td>3</td>
<td>5</td>
<td>1</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
