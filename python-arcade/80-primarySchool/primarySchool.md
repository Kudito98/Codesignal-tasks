<p>Tomorrow is Jim's first day as a teacher in a primary school. He's quite nervous about his new job, and in order to relax he decides to write a simple program, because nothing calms as much as coding.</p>
<p>Since Jim is going to tell the kids about rectangles, he wants to implement a function that will calculate the area of rectangle of the given <code>height</code> and <code>width</code> and show how the result is obtained. Help Jim to gain his confidence and implement the function he needs.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>height = 7</code> and <code>width = 4</code>, the output should be<br />
<code>solution(height, width) = "7 x 4 = 28"</code>.</p>
<p>The area of the rectangle of size <code>7 × 4</code> is calculated as <code>7 * 4</code> and is equal to <code>28</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer height</strong></p>
<p>The height of the rectangle.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ height ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer width</strong></p>
<p>The width of the rectangle.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ width ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A string containing the area of the given rectangle and how it was obtained in the format <code>"<em>height</em> x <em>width</em> = <em>area</em>"</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
