<p>Define <em>crossover operation</em> over two equal-length strings <code>A</code> and <code>B</code> as follows:</p>
<ul>
<li>the result of that operation is a string of the same length as the input strings</li>
<li><code>result[i]</code> is either A[i] or B[i], chosen at random</li>
</ul>
<p>Given array of strings <code>inputArray</code> and a string <code>result</code>, find for how many pairs of strings from <code>inputArray</code> the result of the crossover operation over them may be equal to <code>result</code>.</p>
<p>Note that <code>(A, B)</code> and <code>(B, A)</code> are the same pair. Also note that the pair cannot include the same element of the array twice (however, if there are two equal elements in the array, they can form a pair).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>inputArray = ["abc", "aaa", "aba", "bab"]</code> and <code>result = "bbb"</code>, the output should be<br />
<code>solution(inputArray, result) = 2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string inputArray</strong></p>
<p>A non-empty array of equal-length strings.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ inputArray.length ≤ 10</code>,<br />
<code>1 ≤ inputArray[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string result</strong></p>
<p>A string of the same length as each of the <code>inputArray</code> elements.</p>
<p><em>Guaranteed constraints:</em><br />
<code>result.length = inputArray[i].length</code>.</p>
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
