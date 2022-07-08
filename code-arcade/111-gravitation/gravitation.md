<p>You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
</code></pre>
<p>the output should be <code>solution(rows) = [1, 4]</code>.</p>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/gravitation/img/example.png?_tm=1624642297067" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string rows</strong></p>
<p>A non-empty array of strings of equal length consisting only of <code>#</code>-s and <code>.</code>-s describing the box at a specific moment in time. Sharps represent stones, and dots represent empty cells. <code>row[0]</code> corresponds to the upper row. Last element of <code>rows</code> corresponds to the ground level.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ rows.length ≤ 100</code>,<br />
<code>2 ≤ rows[i].length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array containing numbers of all columns (leftmost column's number is <code>0</code>) in which movements will stop at the same second and earlier than in any other column. Assume that if there are no stones in a column then movement stops immediately, i.e. after <code>0</code> seconds.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
