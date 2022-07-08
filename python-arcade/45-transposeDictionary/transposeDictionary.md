<p>You're implementing a plugin for your favorite code editor. This plugin launches various scripts depending on the open file extension. Each script is associated with exactly one extension, and the information about which script should be launched for each extension is stored in a dictionary <code>scriptByExtension</code>.</p>
<p>You are planning to add more supported extensions for some scripts, so now you would also like to store information about the extensions which each script supports. As a starting point, you'd like to obtain the <code>(<em>extension</em>, <em>script</em>)</code> pairs from the dictionary, sorted <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a> by the <em>extensions</em>.</p>
<p>Implement a function that will do the job.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
</code></pre>
<p>the output should be</p>
<pre><code>solution(scriptByExtension) = [["json", "generateOutputs"], 
                                          ["md", "getLimits"], 
                                          ["py", "validate"]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] dictionary scriptByExtension</strong></p>
<p>The initial dictionary. Both keys and values of the dictionary are guaranteed to be strings that contain only English letters. It is also guaranteed that all dictionary values are unique.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ scriptByExtension.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Array of pairs <code>[<em>extension</em>, <em>script</em>]</code>, sorted <em>lexicographically</em> by the <code><em>extension</em></code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
