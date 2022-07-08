<p>You recently started working at a promising new startup. Now that you're at the end of the first week, you're surprised the product is still working at all: there are bugs in almost every one of its components!</p>
<p>Information about all bugs is stored in a table <strong>Bug</strong>, and information about components is stored in a <strong>Component</strong> table. Since some bugs may be present in several components and vice versa, the additional <strong>BugComponent</strong> table contains rows representing connections between bugs and components. In the database the tables are stored as follows:</p>
<ul>
<li><strong>Bug</strong>:
<ul>
<li><code>num</code>: unique bug number</li>
<li><code>title</code>: bug title</li>
</ul>
</li>
<li><strong>Component</strong>:
<ul>
<li><code>id</code>: unique component id</li>
<li><code>title</code>: component title</li>
</ul>
</li>
<li><strong>BugComponent</strong>:
<ul>
<li><code>bug_num</code>: foreign key referencing <code>Bug.num</code></li>
<li><code>component_id</code>: foreign key referencing <code>Component.id</code></li>
</ul>
</li>
</ul>
<p>There are so many bugs that you don't know what to begin with. To help yourself decide, you want to find all bugs that affect more than one component, and find these components' names. Since it's difficult to test too buggy components, you also want to know how many bugs each such component has. Write a select statement which returns the following columns:</p>
<ul>
<li><code>bug_title</code>: bug title</li>
<li><code>component_title</code>: title of the component to which this bug belongs</li>
<li><code>bugs_in_component</code>: total number of bugs in this component</li>
</ul>
<p>The results should be sorted by the number of bugs in the component in the descending order. In case of a tie, the component with the smallest <code>id</code> should go first. In case it's not enough to break a tie, <code>bug_num</code> should be a tie-breaker: the <code>bug</code> with the smallest <code>num</code> should go first.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>Bug</strong></p>
<table>
<tr>
<td bgcolor="silver" class="medium">num</td>
<td bgcolor="silver" class="medium">title</td>
</tr>
<tr>
<td class="normal">1</td>
<td class="normal">Quotes don't work</td>
</tr>
<tr>
<td class="normal">2</td>
<td class="normal">Highlighting looks weird</td>
</tr>
<tr>
<td class="normal">3</td>
<td class="normal">Posts are not automatically updated</td>
</tr>
<tr>
<td class="normal">4</td>
<td class="normal">Author link doesn't work</td>
</tr>
</table>
, <b>Component</b>
<table>
<tr>
<td bgcolor="silver" class="medium">id</td>
<td bgcolor="silver" class="medium">title</td>
</tr>
<tr>
<td class="normal">1</td>
<td class="normal">Forum</td>
</tr>
<tr>
<td class="normal">2</td>
<td class="normal">Code editor</td>
</tr>
</table>
 and <b>BugComponent</b>
 <table>
<tr>
<td bgcolor="silver" class="medium">bug_num</td>
<td bgcolor="silver" class="medium">component_id</td>
</tr>
<tr>
<td class="normal">1</td>
<td class="normal">1</td>
</tr>
<tr>
<td class="normal">2</td>
<td class="normal">1</td>
</tr>
<tr>
<td class="normal">2</td>
<td class="normal">2</td>
</tr>
<tr>
<td class="normal">3</td>
<td class="normal">1</td>
</tr>
<tr>
<td class="normal">4</td>
<td class="normal">2</td>
</tr>
<tr>
<td class="normal">4</td>
<td class="normal">1</td>
</tr>
</table>
the resulting table should be
<table>
<tr>
<td bgcolor="silver" class="medium">bug_title</td>
<td bgcolor="silver" class="medium">component_title</td>
<td bgcolor="silver" class="medium">bugs_in_component</td>
</tr>
<tr>
<td class="normal">Highlighting looks weird</td>
<td class="normal">Forum</td>
<td class="normal">4</td>
</tr>
<tr>
<td class="normal">Author link doesn't work</td>
<td class="normal">Forum</td>
<td class="normal">4</td>
</tr>
<tr>
<td class="normal">Highlighting looks weird</td>
<td class="normal">Code editor</td>
<td class="normal">2</td>
</tr>
<tr>
<td class="normal">Author link doesn't work</td>
<td class="normal">Code editor</td>
<td class="normal">2</td>
</tr>
</table>
<p>Bugs <code>2</code> (<code>Highlighting looks weird</code>) and <code>4</code> (<code>Author link doesn't work</code>) affect both components, so they should be included in the resulting table. The number of bugs in <code>Forum</code> is <code>4</code>, and in <code>Code editor</code> is <code>2</code>.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
