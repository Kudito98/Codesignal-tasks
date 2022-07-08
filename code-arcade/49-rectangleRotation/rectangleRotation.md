<p>A rectangle with sides equal to even integers <code>a</code> and <code>b</code> is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point <code>(0, 0)</code>, but the sides of the rectangle are not parallel to the axes; instead, they are forming <code>45</code> degree angles with the axes.</p>
<p>How many points with integer coordinates are located inside the given rectangle (including on its sides)?</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = 6</code> and <code>b = 4</code>, the output should be<br />
<code>solution(a, b) = 23</code>.</p>
<p>The following picture illustrates the example, and the <code>23</code> points are marked green.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/rectangleRotation/img/rectangle.png?_tm=1624664766833" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p>A positive even integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ a ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p>A positive even integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ b ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of inner points with integer coordinates.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
