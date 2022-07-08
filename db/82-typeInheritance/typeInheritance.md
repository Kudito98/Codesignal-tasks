<p>You are writing a <em>transcompiler</em> that will be able to translate programs from one programming language to another. Your transcompiler needs to be able to analyze a program to understand what data types it uses and how they should be mapped to the types of the output language.</p>
<p>In order to handle this, you created an <strong>inheritance</strong> table, which has the following structure:</p>
<ul>
<li><code>derived</code>: a unique data type in the original language;</li>
<li><code>base</code>: the base data type from which the <code>derived</code> type is inherited.</li>
</ul>
<p>It's guaranteed that there are no cyclic dependencies.</p>
<p>For each translated program a <strong>variables</strong> table is created, which has the following structure:</p>
<ul>
<li><code>var_name</code>: the unique variable name;</li>
<li><code>type</code>: the variable type.</li>
</ul>
<p>Your task is to write a query that will find the variables of types that are <strong>inherited</strong> from the <code>Number</code> type. The resulting table should contain <code>var_name</code> and <code>var_type</code> columns and be sorted by <code>var_name</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For given tables <strong>inheritance</strong></p>
<table>
<tr>
<th>derived</th>
<th>base</th>
</tr>
<tr>
<td>Double</td>
<td>Number</td>
</tr>
<tr>
<td>Int</td>
<td>Number</td>
</tr>
<tr>
<td>Int64</td>
<td>Int</td>
</tr>
<tr>
<td>Number</td>
<td>Object</td>
</tr>
</table>
<p>and <strong>variables</strong></p>
<table>
<tr>
<th>var_name</th>
<th>type</th>
</tr>
<tr>
<td>A</td>
<td>Int</td>
</tr>
<tr>
<td>B</td>
<td>Object</td>
</tr>
<tr>
<td>C</td>
<td>Double</td>
</tr>
<tr>
<td>D</td>
<td>Int64</td>
</tr>
<tr>
<td>E</td>
<td>Number</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>var_name</th>
<th>var_type</th>
</tr>
<tr>
<td>A</td>
<td>Int</td>
</tr>
<tr>
<td>C</td>
<td>Double</td>
</tr>
<tr>
<td>D</td>
<td>Int64</td>
</tr>
</table>
<p>Type <code>Int64</code> is inherited from type <code>Int</code>, which in turn is inherited from <code>Number</code> type, so both variables <code>A</code> and <code>D</code> should be included in the result. <code>Double</code> type is also inherited from <code>Number</code>, so <code>C</code> is also present in the resulting table.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
