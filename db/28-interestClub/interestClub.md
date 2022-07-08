<p>You are the chairman of your university's drawing club, which isn't doing very well right now. The club meets two times a week to exchange drawing advice, talk about new techniques, and draw something together. But the members are starting to get bored during these meetings, so you've decided to add an additional activity to the routine.</p>
<p>In order to do this, you decided to collect information about the students, which is now stored in the table <strong>people_interests</strong>, which has the following columns:</p>
<ul>
<li><code>name</code> - the unique name of a person;</li>
<li><code>interests</code> - the set of interests or hobbies this person has, given as a comma-joined string. This column has datatype <code>set('reading','sports','swimming','drawing','writing','acting','cooking','dancing','fishkeeping','juggling','sculpting','videogaming')</code>.</li>
</ul>
<p>This information gave you the idea that reading might be an interesting theme for the next meeting, so you announced that the next meeting will be reading-related. Now you're interested in the number of members that will come.</p>
<p>Given the <strong>people_interests</strong> table, find the people who will attend the next meeting, i.e. those who are fond of both drawing and reading. The resulting table should consist of a single <code>name</code> column, and the records should be sorted by people's names.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For given table <strong>people_interests</strong></p>
<table>
<tr>
<th>name</th>
<th>interests</th>
</tr>
<tr>
<td>August</td>
<td>cooking,juggling</td>
</tr>
<tr>
<td>Buddy</td>
<td>reading,swimming,drawing,acting,dancing,videogaming</td>
</tr>
<tr>
<td>David</td>
<td>juggling,sculpting</td>
</tr>
<tr>
<td>Dennis</td>
<td>swimming,cooking,fishkeeping</td>
</tr>
<tr>
<td>James</td>
<td>reading,drawing</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>name</th>
</tr>
<tr>
<td>Buddy</td>
</tr>
<tr>
<td>James</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
