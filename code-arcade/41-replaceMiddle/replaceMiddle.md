<p>We define the <em>middle</em> of the array <code>arr</code> as follows:</p>
<ul>
<li>if <code>arr</code> contains an odd number of elements, its <em>middle</em> is the element whose index number is the same when counting from the beginning of the array and from its end;</li>
<li>if <code>arr</code> contains an even number of elements, its <em>middle</em> is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.</li>
</ul>
<p>Given array <code>arr</code>, your task is to find its <em>middle</em>, and, if it consists of two elements, replace those elements with the value of <em>middle</em>. Return the resulting array as the answer.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>arr = [7, 2, 2, 5, 10, 7]</code>, the output should be<br />
<code>solution(arr) = [7, 2, 7, 10, 7]</code>.</p>
<p>The <em>middle</em> consists of two elements, <code>2</code> and <code>5</code>. These two elements should be replaced with their sum, i.e. <code>7</code>.</p>
</li>
<li>
<p>For <code>arr = [-5, -5, 10]</code>, the output should be<br />
<code>solution(arr) = [-5, -5, 10]</code>.</p>
<p>The <em>middle</em> is defined as a single element <code>-5</code>, so the initial array with no changes should be returned.</p>
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
<code>2 ≤ arr.length ≤ 10<sup>4</sup></code>,<br />
<code>-10<sup>3</sup> ≤ arr[i] ≤ 10<sup>3</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p><code>arr</code> with its <em>middle</em> replaced by a single element, or the initial array if the <em>middle</em> consisted of a single element to begin with.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
