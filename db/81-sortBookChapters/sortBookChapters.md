<p>You found a really old computer at your local library, and it looks like there's still some data about old library books left on its hard drive.</p>
<p>After closer examination, you've discovered that there is a <strong>book_chapters</strong> table, which has the following structure:</p>
<ul>
<li><code>chapter_name</code>: the name of the book's chapter;</li>
<li><code>chapter_number</code>: the unique number of the chapter written as a <a href="https://en.wikipedia.org/wiki/Roman_numerals" target="_blank">Roman numeral</a>.</li>
</ul>
<p>Note that there could be gaps in chapter numbers. Also, every library book has fewer than <code>1000</code> chapters.</p>
<p>Here is the table of Roman numeral symbols and their values:</p>
<table><tr><th>Symbol</th><th>Value</th></tr>
<tr>
  <td>I</td>
  <td>1</td>
</tr>
<tr>
  <td>V</td>
  <td>5</td>
</tr>
<tr>
  <td>X</td>
  <td>10</td>
</tr>
<tr>
  <td>L</td>
  <td>50</td>
</tr>
<tr>
  <td>C</td>
  <td>100</td>
</tr>
<tr>
  <td>D</td>
  <td>500</td>
</tr>
<tr>
  <td>M</td>
  <td>1000</td>
</tr>
</table>
<p>After looking through the library, you've found what seems to be the remnants of this same book! Unfortunately its chapters are not numbered on the pages.</p>
<p>You decide to find the order in which you should read the books chapters by using the old computer and the information stored in the <strong>book_chapters</strong> table.</p>
<p>Given the <strong>book_chapters</strong> table, compose a results table that consists of a single column <code>chapter_name</code> that contains the names of the book's chapters. The table should be sorted in ascending order by the chapter's actual numbers (i.e. chapter number <code>III</code> should come before chapter number <code>V</code>).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>book_chapters</strong></p>
<table>
<tr>
<th>chapter_name</th>
<th>chapter_number</th>
</tr>
<tr>
  <td>A Dead Man</td>
  <td>LVI</td>
</tr>
<tr>
  <td>Behaviour in General</td>
  <td>I</td>
</tr>
<tr>
  <td>Cast Up</td>
  <td>XLIX</td>
</tr>
<tr>
  <td>Imitation</td>
  <td>IX</td>
</tr>
<tr>
  <td>Nemesis</td>
  <td>L</td>
</tr>
<tr>
  <td>Paste</td>
  <td>XXIII</td>
</tr>
<tr>
  <td>The Cub</td>
  <td>XXI</td>
</tr>
<tr>
  <td>The Oxenham Arms</td>
  <td>XXIV</td>
</tr>
<tr>
  <td>Two Bequests</td>
  <td>XLVII</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>chapter_name</th>
</tr>
<tr>
  <td>Behaviour in General</td>
</tr>
<tr>
  <td>Imitation</td>
</tr>
<tr>
  <td>The Cub</td>
</tr>
<tr>
  <td>Paste</td>
</tr>
<tr>
  <td>The Oxenham Arms</td>
</tr>
<tr>
  <td>Two Bequests</td>
</tr>
<tr>
  <td>Cast Up</td>
</tr>
<tr>
  <td>Nemesis</td>
</tr>
<tr>
  <td>A Dead Man</td>
</tr>
</table>
<p>Here are the chapter number converted to Hindu-Arabic numerals:</p>
<table>
<tr>
<th>chapter_name</th>
<th>chapter_number</th>
</tr>
<tr>
  <td>A Dead Man</td>
  <td>56</td>
</tr>
<tr>
  <td>Behaviour in General</td>
  <td>1</td>
</tr>
<tr>
  <td>Cast Up</td>
  <td>49</td>
</tr>
<tr>
  <td>Imitation</td>
  <td>9</td>
</tr>
<tr>
  <td>Nemesis</td>
  <td>50</td>
</tr>
<tr>
  <td>Paste</td>
  <td>23</td>
</tr>
<tr>
  <td>The Cub</td>
  <td>21</td>
</tr>
<tr>
  <td>The Oxenham Arms</td>
  <td>24</td>
</tr>
<tr>
  <td>Two Bequests</td>
  <td>47</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
