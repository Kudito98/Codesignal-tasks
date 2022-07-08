<p>You are given an array of integers representing coordinates of obstacles situated on a straight line.</p>
<p>Assume that you are jumping from the point with coordinate <code>0</code> to the right. You are allowed only to make jumps of the same length represented by some integer.</p>
<p>Find the minimal length of the jump enough to avoid all the obstacles.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>inputArray = [5, 3, 6, 7, 9]</code>, the output should be<br />
<code>solution(inputArray) = 4</code>.</p>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1624426122561" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer inputArray</strong></p>
<p>Non-empty array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ inputArray.length ≤ 1000</code>,<br />
<code>1 ≤ inputArray[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The desired length.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
