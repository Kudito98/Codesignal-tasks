<p>The elf factories have already finished producing all Christmas presents, but before Santa can start delivering them they need to be properly packaged.</p>
<p>All produced gifts and available packages are stored in two tables called <strong>gifts</strong> and <strong>packages</strong> respectively, that have the following structures:</p>
<ul>
<li><strong>gifts</strong>:
<ul>
<li><code>id</code>: unique gift id;</li>
<li><code>gift_name</code>: the name of the gift;</li>
<li><code>length</code>: gift length;</li>
<li><code>width</code>: gift width;</li>
<li><code>height</code>: gift height;</li>
</ul>
</li>
<li><strong>packages</strong>:
<ul>
<li><code>package_type</code>: package type;</li>
<li><code>length</code>: the length of the package;</li>
<li><code>width</code>: the width of the package;</li>
<li><code>height</code>: the height of the package.</li>
</ul>
</li>
</ul>
<p>A gift fits in a package if its <code>length</code>, <code>width</code> and <code>height</code> are equal to or less than <code>length</code>, <code>width</code> and <code>height</code> of the package respectively. Note, that the presents can't be rotated, since some of them are very fragile.</p>
<p>There is not much space on Santa's sleigh, so each gift is put in the smallest package it fits. One package is considered to be smaller than the other if its volume is smaller than the volume of the other package. Note, that one package can't hold more than one gift.</p>
<p>Given the tables <strong>gifts</strong> and <strong>packages</strong>, compose the resulting table with two columns: <code>package_type</code> and <code>number</code>. The first column should contain the <code>package_type</code> of the package, and the second one should contain the number of the packages with such <code>package_type</code> that will be used for packaging Christmas gifts in the manner described above. If package of some type wasn't used at all it shouldn't be included in the result.</p>
<p>The result should be sorted by the <code>package_type</code> in <em>ascending</em> order.<br />
It is guaranteed that each gift fits some package and that there are no package <code>types</code> with the same volume.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>gifts</strong></p>
<table>
<tr>
<th>id</th>
<th>gift_name</th>
<th>length</th>
<th>width</th>
<th>height</th>
</tr>
<tr>
  <td>1</td>
  <td>Water gun</td>
  <td>3</td>
  <td>1</td>
  <td>1</td>
</tr>
<tr>
  <td>2</td>
  <td>Video game</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
</tr>
<tr>
  <td>3</td>
  <td>Toy car</td>
  <td>4</td>
  <td>2</td>
  <td>2</td>
</tr>
<tr>
  <td>4</td>
  <td>Toy car</td>
  <td>4</td>
  <td>2</td>
  <td>2</td>
</tr>
<tr>
  <td>5</td>
  <td>Toy gun</td>
  <td>2</td>
  <td>1</td>
  <td>1</td>
</tr>
</table>
<p>and <strong>packages</strong></p>
<table>
<tr>
<th>package_type</th>
<th>length</th>
<th>width</th>
<th>height</th>
</tr>
<tr>
  <td>big</td>
  <td>4</td>
  <td>4</td>
  <td>4</td>
</tr>
<tr>
  <td>extra</td>
  <td>5</td>
  <td>5</td>
  <td>5</td>
</tr>
<tr>
  <td>medium</td>
  <td>2</td>
  <td>2</td>
  <td>2</td>
</tr>
<tr>
  <td>small</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
</tr>
<tr>
  <td>special</td>
  <td>4</td>
  <td>3</td>
  <td>1</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>package_type</th>
<th>number</th>
</tr>
<tr>
  <td>big</td>
  <td>2</td>
</tr>
<tr>
  <td>medium</td>
  <td>1</td>
</tr>
<tr>
  <td>small</td>
  <td>1</td>
</tr>
<tr>
  <td>special</td>
  <td>1</td>
</tr>
</table>
<p>because here is how the presents will be packaged:</p>
<table>
<tr>
<th>gift id</th>
<th>its package</th>
</tr>
<tr>
  <td>1</td>
  <td>special</td>
</tr>
<tr>
  <td>2</td>
  <td>small</td>
</tr>
<tr>
  <td>3</td>
  <td>big</td>
</tr>
<tr>
  <td>4</td>
  <td>big</td>
</tr>
<tr>
  <td>5</td>
  <td>medium</td>
</tr>
</table>
<p>Note, that there is no row for <code>extra</code> package type in the output, since it won't be used.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
