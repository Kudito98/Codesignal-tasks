<p>Yesterday you wrote down the links for some resources that you are going to use as references in your academic paper, and now you want to sort them. You didn't bother to write down the entire link for any of them, so all you have is a bunch of unique hostnames.</p>
<p>You stored the information about these hostnames in the table <strong>hostnames</strong>, which has the structure:</p>
<ul>
<li><code>id</code>: the unique hostname id;</li>
<li><code>hostname</code>: the unique hostname.</li>
</ul>
<p>Each hostname contain several domains and can be written in the format <code>hostname = domain<sub>1</sub>.domain<sub>2</sub>. ...</code>. To sort the hostnames, you've decided that hostname <code>A</code> should go before hostname <code>B</code> in the sorted list if its reversed list of domains is <a href="keyword://lexicographical-order-for-arrays" target="_blank">lexicographically smaller</a> than the reversed list of <code>B</code>'s domains.</p>
<p>Given the table <strong>hostnames</strong>, write a select statement as follows: The output should have columns <code>id</code> and <code>hostname</code>, and its values should be ordered as described above. It is guaranteed that all the hostnames are different and that there are no more than <code>3</code> domains in each hostname.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>hostnames</strong></p>
<table>
  <tr>
    <th>id</th>
    <th>hostname</th>
  </tr>
  <tr>
    <td>1</td>
    <td>workbench.mysql.com</td>
  </tr>
  <tr>
    <td>2</td>
    <td>codesignal.slack.com</td>
  </tr>
  <tr>
    <td>3</td>
    <td>codesignal.com</td>
  </tr>
  <tr>
    <td>4</td>
    <td>snarknews.info</td>
  </tr>
  <tr>
    <td>5</td>
    <td>sololearn.com</td>
  </tr>
  <tr>
    <td>6</td>
    <td>dev.mysql.com</td>
  </tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>hostname</th>
</tr>
<tr>
<td>3</td>
<td>codesignal.com</td>
</tr>
<tr>
<td>6</td>
<td>dev.mysql.com</td>
</tr>
<tr>
<td>1</td>
<td>workbench.mysql.com</td>
</tr>
<tr>
<td>2</td>
<td>codesignal.slack.com</td>
</tr>
<tr>
<td>5</td>
<td>sololearn.com</td>
</tr>
<tr>
<td>4</td>
<td>snarknews.info</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
