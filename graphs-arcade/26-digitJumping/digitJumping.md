<p>Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.</p>
<p>Facing his first challenge, Ratiorg is placed at the <code>start</code> position of a rectangular <code>grid</code> filled with digits from <code>0</code> to <code>9</code>. With each move, Ratiorg can either jump to the adjacent cell (the one above, below, to the left or to the right of his current position), or teleport to any cell that has number <code>x</code> written on it, where <code>x</code> is the number written on the cell Ratiorg is currently standing on. Ratiorg will be able to move on to the next challenge if he manages to get to the <code>finish</code> cell in the minimum possible number of moves.</p>
<p>Although the little bot is sure that he can handle the challenge, you don't want to leave him alone! Back Ratiorg up by implementing a function that given the <code>grid</code>, <code>start</code> and <code>finish</code>, will calculate the minimum number of moves required to get from <code>start</code> to <code>finish</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>grid = [[0, 1, 4, 2, 3],
        [1, 4, 2, 8, 2],
        [2, 2, 3, 4, 9],
        [8, 7, 2, 2, 3]]
</code></pre>
<p><code>start = [0, 0]</code>, and <code>finish = [3, 4]</code>, the output should be<br />
<code>solution(grid, start, finish) = 4</code>.</p>
<p>Here's one of the shortest paths Ratiorg can take:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/digitJumping/img/example.png?_tm=1624350029178" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer grid</strong></p>
<p>A rectangular grid filled with digits in range <code>[0...9]</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ grid.length ≤ 300</code>,<br />
<code>1 ≤ grid[0].length ≤ 300</code>,<br />
<code>0 ≤ grid[i][j] ≤ 9</code>.</p>
</li>
<li>
<p><strong>[input] array.integer start</strong></p>
<p>Ratiorg's initial position as an array of two elements, where the first element is row index, and the second one is column index.</p>
<p><em>Guaranteed constraints:</em><br />
<code>start.length = 2</code>,<br />
<code>0 ≤ start[0] &lt; grid.length</code>,<br />
<code>0 ≤ start[1] &lt; grid[0].length</code>.</p>
</li>
<li>
<p><strong>[input] array.integer finish</strong></p>
<p>Ratioarg's destination in the same format as <code>start</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>finish.length = 2</code>,<br />
<code>0 ≤ finish[0] &lt; grid.length</code>,<br />
<code>0 ≤ finish[1] &lt; grid[0].length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum number of moves required to get from <code>start</code> to <code>finish</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
