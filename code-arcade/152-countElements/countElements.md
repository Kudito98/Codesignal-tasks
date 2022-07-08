<p>You've been invited to a job interview at a famous company that tests programming challenges. To evaluate your coding skills, they have asked you to parse a given problem's input given as an <code>inputString</code> string, and count the number of <em>primitive type</em> elements within it.</p>
<p>The <code>inputString</code> can be either a <em>primitive type</em> variable or an array (possibly multidimensional) that contains elements of the <em>primitive types</em>.<br />
A <em>primitive type</em> variable can be:</p>
<ul>
<li>an integer number;</li>
<li>a string, which is surrounded by <code>"</code> characters (note that it may contain <strong>any</strong> character except <code>"</code>);</li>
<li>a boolean, which is either <code>true</code> or <code>false</code>.</li>
</ul>
<p>Return the total number of <em>primitive type</em> elements inside <code>inputString</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>inputString = "[[0, 20], [33, 99]]"</code>, the output should be<br />
<code>solution(inputString) = 4</code>;</li>
<li>For <code>inputString = "[ "one", 2, "three" ]"</code>, the output should be<br />
<code>solution(inputString) = 3</code>;</li>
<li>For <code>inputString = "true"</code>, the output should be<br />
<code>solution(inputString) = 1</code>;</li>
<li>For <code>inputString = "[[1, 2, [3]], 4]"</code>, the output should be<br />
<code>solution(inputString) = 4</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string inputString</strong></p>
<p>Correct input of a given problem.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ inputString.length ≤ 60</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The total number of <em>primitive type</em> elements within the input.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
