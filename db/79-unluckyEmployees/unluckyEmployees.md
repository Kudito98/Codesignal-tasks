<p>Your company has fallen on hard times, and you have to let some of your employees go. You figure it will be easier to fire an entire department all at once, so now you want to determine which department it's going to be.</p>
<p>Information about your employees and departments is stored in two tables, <strong>Employee</strong> and <strong>Department</strong>, respectively. Here are their structures:</p>
<ul>
<li><strong>Department</strong>:
<ul>
<li><code>id</code>: unique department id</li>
<li><code>name</code>: department name</li>
</ul>
</li>
<li><strong>Employee</strong>:
<ul>
<li><code>id</code>: unique employee id</li>
<li><code>full_name</code>: employee's full name</li>
<li><code>department</code>: foreign key referencing <code>Department.id</code></li>
<li><code>salary</code>: employee's salary</li>
</ul>
</li>
</ul>
<p>To choose the unfortunate department, you set a number of criteria: you are willing to get rid of any department that has no more than <code>5</code> employees. Among these smaller departments, you will consider those where the total salary of all its employees is maximal. Lastly, to make a tough situation more fair, you decide to make the final choice from the remaining departments at random. Thus, you'd like to write a select statement that lists departments:</p>
<ul>
<li>select all departments with less than <code>6</code> employees;</li>
<li>sort these departments by the total salary of its workers in descending order (in the case of a tie, the department with the greatest number of employees should go first; if it's still not enough to break a tie, the department with the smallest <code>id</code> should go first);</li>
<li>cross out the departments at the even rows and leave only those in the odd positions, to consider them more thoroughly afterwards.</li>
</ul>
<p>Given tables <strong>Employee</strong> and <strong>Department</strong>, write the needed select statement. The output should have columns <code>dep_name</code>, <code>emp_number</code> and <code>total_salary</code> and be sorted as described above.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>Department</strong></p>
<table>
  <tr>
    <th>id</th>
    <th>name</th>
  </tr>
  <tr>
    <td>1</td>
    <td>IT</td>
  </tr>
  <tr>
    <td>2</td>
    <td>HR</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Sales</td>
  </tr>
</table>
<p>and <b>Employee</b></p>
<table>
<tr>
<th>id</th>
<th>full_name</th>
<th>salary</th>
<th>department</th>
</tr>
<tr>
<td>1</td>
<td>James Smith</td>
<td>20</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>John Johnson</td>
<td>13</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>Robert Jones</td>
<td>15</td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>Michael Williams</td>
<td>15</td>
<td>1</td>
</tr>
<tr>
<td>5</td>
<td>Mary Troppins</td>
<td>17</td>
<td>1</td>
</tr>
<tr>
<td>8</td>
<td>Penny Old</td>
<td>14</td>
<td>2</td>
</tr>
<tr>
<td>9</td>
<td>Richard Young</td>
<td>17</td>
<td>2</td>
</tr>
<tr>
<td>10</td>
<td>Drew Rich</td>
<td>50</td>
<td>3</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>dep_name</th>
<th>emp_number</th>
<th>total_salary</th>
</tr>
<tr>
<td>IT</td>
<td>5</td>
<td>80</td>
</tr>
<tr>
<td>HR</td>
<td>2</td>
<td>31</td>
</tr>
</table>
<p>All three departments have <code>5</code> or fewer employees, so they are all candidates to be fired. When sorted in descending order by <code>total_salary</code>, the <code>Sales</code> department becomes the second (i.e. is located at an even row), so it's not present in the resulting table.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
