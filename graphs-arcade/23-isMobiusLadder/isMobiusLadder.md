<p>You've been studying trees a lot lately, and became an expert in caterpillar trees. Now that you know everything about them, you're ready to climb one. However, in order to climb such tree you need a special ladder that you call a <em>mobius ladder</em>.</p>
<p>A <em>mobius ladder</em> is a slightly modified <em>proper ladder</em>. Firstly, let's define what <em>proper ladder</em> is: a <em>proper ladder</em> is a ladder that can be represented by a graph containing two chains of vertices with <code>n</code> vertices in each one, where the <code>i<sup>th</sup></code> vertex of the first chain is connected to the <code>i<sup>th</sup></code> vertex of the second chain. For example, a <em>proper ladder</em> with <code>8</code> vertices looks like this:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isMobiusLadder/img/ladder.png?_tm=1624357933697" alt /></p>
<p>A <em>mobius ladder</em> is a <em>proper ladder</em> with two more connections: the first vertex of the first chain is connected to the last vertex of the second chain, and last vertex of the first chain is connected to the first vertex of the second chain. For example, here is a <em>mobius ladder</em> with <code>8</code> vertices:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isMobiusLadder/img/mobius_ladder.png?_tm=1624357933914" alt /></p>
<p>You found a <code>ladder</code> that can be represented by <code>n</code> vertices in the attic. Now you need to check if it is a <em>mobius ladder</em>, to make sure it can be used to climb a caterpillar tree.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 6</code> and <code>ladder = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]</code>, the output should be<br />
<code>solution(n, ladder) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isMobiusLadder/img/example1.png?_tm=1624357934136" alt /></p>
</li>
<li>
<p>For <code>n = 8</code> and</p>
<pre><code>ladder = [[0, 1], [0, 2], [0, 7], [1, 3], [1, 6], [2, 3],
          [2, 4], [3, 5], [4, 5], [4, 6], [5, 7], [6, 7]]
</code></pre>
<p>the output should be <code>solution(n, ladder) = true</code>.</p>
<p>This is the test from the description:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isMobiusLadder/img/example2.png?_tm=1624357934372" alt /></p>
</li>
<li>
<p>For <code>n = 10</code> and</p>
<pre><code>ladder = [[0, 1], [0, 3], [0, 7], [0, 9], [1, 2],
          [1, 4], [1, 8], [2, 3], [2, 5], [2, 9],
          [3, 4], [3, 6], [4, 5], [4, 7], [5, 6],
          [5, 8], [6, 7], [6, 9], [7, 8], [8, 9]]
</code></pre>
<p>the output should be <code>solution(n, ladder) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isMobiusLadder/img/example3.png?_tm=1624357934623" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>An even integer, the number of vertices that represent your ladder.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ n ≤ 5 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer ladder</strong></p>
<p>Edges of the ladder drawn in the plan. <code>ladder[i]</code> for each valid <code>i</code> contains two elements and represents an edge that connects <code>ladder[i][0]</code> and <code>ladder[i][1]</code>.<br />
It is guaranteed that between any two vertices there is no more than one edge.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ ladder.length ≤ 75000</code>,<br />
<code>ladder[i].length = 2</code>,<br />
<code>0 ≤ ladder[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given <code>ladder</code> represents a <em>mobius ladder</em>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
