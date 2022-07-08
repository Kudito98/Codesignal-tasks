<p>In <em>ChessLand</em> there is a small but proud chess bishop with a recurring dream. In the dream the bishop finds itself on an <code>n × m</code> chessboard with mirrors along each edge, and it is not a bishop but a ray of light. This ray of light moves only along diagonals (the bishop can't imagine any other types of moves even in its dreams), it never stops, and once it reaches an edge or a corner of the chessboard it reflects from it and moves on.</p>
<p>Given the initial position and the direction of the ray, find its position after <code>k</code> steps where a step means either moving from one cell to the neighboring one or reflecting from a corner of the board.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>boardSize = [3, 7]</code>, <code>initPosition = [1, 2]</code>,<br />
<code>initDirection = [-1, 1]</code>, and <code>k = 13</code>, the output should be<br />
<code>solution(boardSize, initPosition, initDirection, k) = [0, 1]</code>.</p>
<p>Here is the bishop's path:</p>
<pre><code>[1, 2] -&gt; [0, 3] -(reflection from the top edge)-&gt; [0, 4] -&gt; 
[1, 5] -&gt; [2, 6] -(reflection from the bottom right corner)-&gt; [2, 6] -&gt;
[1, 5] -&gt; [0, 4] -(reflection from the top edge)-&gt; [0, 3] -&gt;
[1, 2] -&gt; [2, 1] -(reflection from the bottom edge)-&gt; [2, 0] -(reflection from the left edge)-&gt;
[1, 0] -&gt; [0, 1]
</code></pre>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessBishopDream/img/example.png?_tm=1624649134576" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer boardSize</strong></p>
<p>An array of two integers, the number of rows and columns, respectively. Rows are numbered by integers from <code>0</code> to <code>boardSize[0] - 1</code>, columns are numbered by integers from <code>0</code> to <code>boardSize[1] - 1</code> (both inclusive).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ boardSize[i] ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] array.integer initPosition</strong></p>
<p>An array of two integers, indices of the row and the column where the bishop initially stands, respectively.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ initPosition[i] &lt; boardSize[i]</code>.</p>
</li>
<li>
<p><strong>[input] array.integer initDirection</strong></p>
<p>An array of two integers representing the initial direction of the bishop. If it stands in <code>(a, b)</code>, the next cell he'll move to is <code>(a + initDirection[0], b + initDirection[1])</code> or whichever it'll reflect to in case it runs into a mirror immediately.</p>
<p><em>Guaranteed constraints:</em><br />
<code>initDirection[i] ∈ {-1, 1}</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ k ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The position of the bishop after <code>k</code> steps.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
