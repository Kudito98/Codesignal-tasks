<p>You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.</p>
<p>Find the perimeter of the black figure assuming that a single cell has unit length.</p>
<p>It's guaranteed that there is at least one black cell on the table.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
</code></pre>
<p>the output should be<br />
<code>solution(matrix) = 12</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/polygonPerimeter/img/example1.png?_tm=1624663868339" alt /></p>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
</code></pre>
<p>the output should be<br />
<code>solution(matrix) = 16</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/polygonPerimeter/img/example2.png?_tm=1624663868623" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean matrix</strong></p>
<p>A matrix of booleans representing the rectangular board where <code>true</code> means a <em>black</em> cell and <code>false</code> means a <em>white</em> one.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ matrix.length ≤ 5</code>,<br />
<code>2 ≤ matrix[0].length ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
