<p>We define the <em>middle</em> of the array <code>arr</code> as follows:</p>
<ul>
<li>if <code>arr</code> contains an odd number of elements, its <em>middle</em> is the element whose index number is the same when counting from the beginning of the array and from its end;</li>
<li>if <code>arr</code> contains an even number of elements, its <em>middle</em> is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.</li>
</ul>
<p>An array is called <em>smooth</em> if its first and its last elements are equal to one another and to the <em>middle</em>. Given an array <code>arr</code>, determine if it is <em>smooth</em> or not.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>arr = [7, 2, 2, 5, 10, 7]</code>, the output should be<br />
<code>solution(arr) = true</code>.</p>
<p>The first and the last elements of <code>arr</code> are equal to <code>7</code>, and its <em>middle</em> also equals <code>2 + 5 = 7</code>. Thus, the array is <em>smooth</em> and the output is <code>true</code>.</p>
</li>
<li>
<p>For <code>arr = [-5, -5, 10]</code>, the output should be<br />
<code>solution(arr) = false</code>.</p>
<p>The first and <em>middle</em> elements are equal to <code>-5</code>, but the last element equals <code>10</code>. Thus, <code>arr</code> is not <em>smooth</em> and the output is <code>false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer arr</strong></p>
<p>The given array.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ arr.length ≤ 10<sup>5</sup></code>,<br />
<code>-10<sup>9</sup> ≤ arr[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>arr</code> is <em>smooth</em>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
