<p>Your company is an authorized Chevrolet dealer, and you have your own database of the clients who've come to you for vehicle inspections. Right now it's not very convenient to analyze because it contains only the information retrieved during each inspection. You'd like to make this database easier to use.</p>
<p>Information about the inspections is given in the table <strong>inspections</strong>, which has the following columns:</p>
<ul>
<li><code>inspection_id</code>: the unique inspection ID;</li>
<li><code>driver_name</code>: the name of the driver;</li>
<li><code>date</code>: the inspection date (guaranteed to be distinct for each driver);</li>
<li><code>miles_logged</code>: the number of miles the vehicle has covered since the previous inspection (or since the time of purchase if it's the car's first inspection).</li>
</ul>
<p>Your goal is to make a new table with a single <code>summary</code> column that contains the following information:</p>
<ul>
<li>The first row should contain the total number of miles covered by all the drivers combined;</li>
<li>The following rows should contain information about each driver, sorted by the drivers' names:
<ul>
<li>The first row should contain the driver's name, the total number of inspections, and the total number of miles covered;</li>
<li>The following rows should, for each inspection, contain the date of the inspection and the miles covered since the previous inspection (or the purchase time). The entries should be sorted by the inspection dates.</li>
</ul>
</li>
</ul>
<p>This information should be given in the following format:</p>
<table>
<tr>
<th>summary</th>
</tr>
<tr>
<td> Total miles driven by all drivers combined: <code>&lt;the sum of all driven miles&gt;</code></td>
</tr>
<tr>
<td> Name: [...]; number of inspections: [...]; miles driven: [...]</td>
</tr>
<tr>
<td>  date: [...]; miles covered: [...]</td>
</tr>
<tr>
<td>  date: [...]; miles covered: [...]</td>
</tr>
<tr>
<td>  ...
</td></tr>
<tr>
<td> Name: [...]; number of inspections: [...]; miles driven: [...]</td>
</tr>
<tr>
<td>  ...</td>
</tr>
</table>
<p><strong>Note:</strong> Every row should start with a whitespace character, and the rows containing information about the inspections should should start with two whitespace characters.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>inspections</strong></p>
<table>
  <tr>
    <th>inspection_id</th>
    <th>driver_name</th>
    <th>date</th>
    <th>miles_logged</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Gary</td>
    <td>2014-03-15</td>
    <td>256</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Dave</td>
    <td>2014-01-18</td>
    <td>231</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Dave</td>
    <td>2014-01-16</td>
    <td>45</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Gary</td>
    <td>2014-02-03</td>
    <td>30</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Dave</td>
    <td>2014-01-17</td>
    <td>180</td>
  </tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>summary</th>
</tr>
<tr>
<td> Total miles driven by all drivers combined: 742</td>
</tr>
<tr>
<td> Name: Dave; number of inspections: 3; miles driven: 456</td>
</tr>
<tr>
<td>  date: 2014-01-16; miles covered: 45</td>
</tr>
<tr>
<td>  date: 2014-01-17; miles covered: 180</td>
</tr>
<tr>
<td>  date: 2014-01-18; miles covered: 231</td>
</tr>
<tr>
<td> Name: Gary; number of inspections: 2; miles driven: 286</td>
</tr>
<tr>
<td>  date: 2014-02-03; miles covered: 30</td>
</tr>
<tr>
<td>  date: 2014-03-15; miles covered: 256</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
