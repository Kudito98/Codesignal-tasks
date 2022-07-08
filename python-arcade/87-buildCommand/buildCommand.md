<p>While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command for your favorite text editor plugin. The build command is stored as a JSON file that you should now update. In order to make the transition simpler, you decided to write a program that will create a template of the build command by replacing everything but dictionaries in given <code>jsonFile</code> with their default values: numbers with <code>0</code>, strings with <code>""</code> and lists with <code>[]</code>.</p>
<p>It is guaranteed that there are only aforementioned types in the given JSON file.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>jsonFile =
"""
{
    "version": "0.1.0",
    "command": "c:python",
    "args": ["app.py"],
    "problemMatcher": {
        "fileLocation": ["relative", "${workspaceRoot}"],
        "pattern": {
            "regexp": "^(.*)+s$",
            "message": 1
        }
    }
}
"""
</code></pre>
<p>the output should be</p>
<pre><code>solution(jsonFile) =
"""
{
    "version": "",
    "command": "",
    "args": [],
    "problemMatcher": {
        "fileLocation": [],
        "pattern": {
            "regexp": "",
            "message": 0
        }
    }
}
"""
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string jsonFile</strong></p>
<p>A correct JSON file of build command for your favorite plugin. It is guaranteed that it contains only lists, dictionaries, strings and numbers. It is also guaranteed that the entire file consists of a single dictionary.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ jsonFile.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Modified <code>jsonFile</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
