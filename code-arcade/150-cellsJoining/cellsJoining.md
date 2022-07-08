<p>You are writing a spreadsheet application for an ancient operating system. The system runs on a computer so old that it can only display ASCII graphics. Currently you are stuck with implementing the cells joining algorithm.</p>
<p>You are given a <code>table</code> in ASCII graphics, where the following characters are used for borders: <code>+</code>, <code>-</code>, <code>|</code>. The rows can have different heights and the columns can have different widths. Each cell has an area greater than <code>1</code> (excluding the borders) and can contain any ASCII characters excluding <code>+</code>, <code>-</code> and <code>|</code>.</p>
<p>The algorithm you want to implement should merge the cells within a given rectangular part of the table into a single cell by removing the borders between them (i.e. replace them with space characters (<code>' '</code>) and replace redundant <code>+</code>s with correct border symbols). The cells to join are represented by the coordinates of the cells at the extreme bottom-left and top-right of the area.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span><br />
For</p>
<pre><code>table = ["+----+--+-----+----+",
         "|abcd|56|!@#$%|qwer|",
         "|1234|78|^&amp;=()|tyui|",
         "+----+--+-----+----+",
         "|zxcv|90|77777|stop|",
         "+----+--+-----+----+",
         "|asdf|~~|ghjkl|100$|",
         "+----+--+-----+----+"]
</code></pre>
<p>and <code>coords = [[2, 0], [1, 1]]</code>, the output should be</p>
<pre><code>solution(table, coords) = ["+----+--+-----+----+",
                               "|abcd|56|!@#$%|qwer|",
                               "|1234|78|^&amp;=()|tyui|",
                               "+----+--+-----+----+",
                               "|zxcv 90|77777|stop|",
                               "|       +-----+----+",
                               "|asdf ~~|ghjkl|100$|",
                               "+-------+-----+----+"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string table</strong></p>
<p>A table in ASCII graphics. <code>'|'</code> and <code>'-'</code> characters represent borders, and <code>'+'</code> characters represent their intersection. It is guaranteed that there are no joined cells in the table. It's also guaranteed that the table occupies the entire rectangular array, i.e. its outer borders occupy the leftmost and the rightmost columns of the array as well as its topmost and bottommost rows.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ table.length ≤ 25</code>,<br />
<code>3 ≤ table[i].length ≤ 80</code>,<br />
<code>table[i].length = table[j].length</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer coords</strong></p>
<p><code>coords[0]</code> contains 0-based row and column indices (given in that exact order) of the extreme bottom left cell in the area to join, and <code>coords[1]</code> contains indices of the extreme top right cell of that region.</p>
<p>It's guaranteed that there are at least two cells to be joined, and that cells with the given indices do exist in the table.</p>
<p>The rows are numbered from top to bottom while the columns are numbered from left to right.</p>
<p><em>Guaranteed constraints:</em><br />
<code>coords.length = 2</code>,<br />
<code>coords[i].length = 2</code>,<br />
<code>0 ≤ coords[1][0] ≤ coords[0][0] &lt; 10</code>,<br />
<code>0 ≤ coords[0][1] ≤ coords[1][1] ≤ 25</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Table with cells in given region joined into one.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
