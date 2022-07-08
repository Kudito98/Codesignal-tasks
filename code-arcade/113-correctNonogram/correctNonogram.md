<p>A <strong>nonogram</strong> is also known as <em>Paint by Numbers</em> and <em>Japanese Crossword</em>. The aim in this puzzle is to color the grid into black and white squares. At the top of each column, and at the side of each row, there are sets of one or more <em>numbers</em> which describe the runs of black squares in that row/column in exact order. For example, if you see <code>10 1</code> along some column/row, this indicates that there will be a run of exactly ten black squares, followed by one or more white squares, followed by a single black square. The cells along the edges of the grid can also be white.</p>
<p>You are given a square <strong>nonogram</strong> of size <code>size</code>. Its grid is given as a square matrix <code>nonogramField</code> of size <code>(size + 1) / 2 + size</code>, where the first <code>(size + 1) / 2</code> cells of each row and and each column define the <em>numbers</em> for the corresponding row/column, and the rest <code>size × size</code> cells define the the grid itself.</p>
<p>Determine if the given <strong>nonogram</strong> has been solved correctly.</p>
<p><em>Note: here <code>/</code> means integer division.</em></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>size = 5</code> and</p>
<pre><code>nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "2", "2", "1", "-", "1"],
                 ["-", "-", "-", "2", "1", "1", "3", "3"],
                 ["-", "3", "1", "#", "#", "#", ".", "#"],
                 ["-", "-", "2", "#", "#", ".", ".", "."],
                 ["-", "-", "2", ".", ".", ".", "#", "#"],
                 ["-", "1", "2", "#", ".", ".", "#", "#"],
                 ["-", "-", "5", "#", "#", "#", "#", "#"]]
</code></pre>
<p>the output should be <code>solution(size, nonogramField) = true</code>;</p>
</li>
<li>
<p>For <code>size = 5</code> and</p>
<pre><code>nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "1", "-", "-"],
                 ["-", "-", "-", "3", "3", "2", "5", "5"],
                 ["-", "-", "3", ".", ".", ".", "#", "#"],
                 ["-", "2", "2", "#", "#", "#", "#", "#"],
                 ["-", "-", "5", "#", "#", "#", "#", "#"],
                 ["-", "-", "5", "#", "#", "#", "#", "#"],
                 ["-", "-", "2", ".", ".", ".", "#", "#"]]
</code></pre>
<p>the output should be <code>solution(size, nonogramField) = false</code>.</p>
<p>There are three mistakes in the <strong>nonogram</strong>:</p>
<ul>
<li>In the <code>5<sup>th</sup></code> (1-based) row there are <em>numbers</em> <code>["-", "2", "2"]</code>, so there should be two runs of <code>2</code> black squares separated by at least one white square. However, there is only one run of <code>5</code> black squares.</li>
<li>In the <code>6<sup>th</sup></code> column there are <em>numbers</em> <code>["-", "1", "2"]</code>, so there should be a run of exactly <code>1</code> black square, followed by one or more white squares, followed by another <code>2</code> black squares. However, there is a single run of <code>3</code> black squares not separated by white ones.</li>
<li>Finally, in the <code>4<sup>th</sup></code> row there are <em>numbers</em> <code>["-", "-", "3"]</code>, so there should be a single run of exactly <code>3</code> black squares. However, there is just a 2-square run in that row.</li>
</ul>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer size</strong></p>
<p>A positive integer, the size of the grid.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ size ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.array.string nonogramField</strong></p>
<p>A square matrix of strings of size <code>(size + 1) / 2 + size</code> defining the puzzle field.<br />
The first <code>(size + 1) / 2</code> cells of each row and each column define the <em>numbers</em> for this row/column. If there is no <em>number</em> in the cell, its value is <code>"-"</code>.<br />
The remaining <code>size × size</code> cells define the grid, where string <code>"#"</code> denotes black cells and string <code>"."</code> denotes white ones.</p>
<p><em>Guaranteed constraints:</em><br />
<code>8 ≤ nonogramField.length ≤ 15</code>,<br />
<code>nonogramField[i].length = nonogramField.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given <strong>nonogram</strong> is solved correctly and <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
