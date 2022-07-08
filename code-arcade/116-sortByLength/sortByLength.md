<p>Given an array of strings, sort them in the order of increasing lengths. If two strings have the same length, their relative order must be the same as in the initial array.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>inputArray = ["abc",
              "",
              "aaa",
              "a",
              "zz"]
</code></pre>
<p>the output should be</p>
<pre><code>solution(inputArray) = ["",
                            "a",
                            "zz",
                            "abc",
                            "aaa"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string inputArray</strong></p>
<p>A non-empty array of strings.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ inputArray.length ≤ 100</code>,<br />
<code>0 ≤ inputArray[i].length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
